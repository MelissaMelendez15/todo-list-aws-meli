pipeline {

    agent any
    options {
        skipDefaultCheckout(true)
    }
    
    environment {
       GITHUB_CREDENTIALS_MELI = credentials('GITHUB_CREDENTIALS_MELI')
       BASE_URL_PROD = credentials('BASE_URL_PROD')
       STAGE = 'production'
   }
   
   stages {
      stage('Get Code'){
         steps {
            checkout([
               $class: 'GitSCM',
               branches: [[name: '*/master']],
               userRemoteConfigs: [[
                   url: 'https://github.com/MelissaMelendez15/todo-list-aws-meli.git',
                   credentialsId: 'GITHUB_CREDENTIALS_MELI'
                ]]
              ])
              
              sh '''
                echo "Descargando configuración desde repo externo..."
                curl -o samconfig.toml https://raw.githubusercontent.com/MelissaMelendez15/todo-list-aws-config/staging/samconfig.toml
                echo "Contenido del samconfig.toml descargando:"
                cat samconfig.toml
              '''
            }
       
       }
       
       stage('Static') {
          agent {
             docker {
                 image 'melissa15/python-static-checker:1.0'
                 reuseNode true
            }
        }
          
          steps {
             
            sh  '''
                 echo "Ejecutando Flake8..."
                 flake8 src/ --exit-zero --format=default > flake8-report.txt || true
                 
                 echo "Ejecutando Bandit..."
                 bandit -r src/ -f txt -o bandit-report.txt || true
             '''
             
             recordIssues tools: [flake8(pattern: 'flake8-report.txt')]
             archiveArtifacts artifacts: 'bandit-report.txt', fingerprint:true
    
            }
        }

        stage('Deploy') {
          
          steps {
             sh  '''
                  echo "Usuario actual:"
                  whoami || echo "No se pudo obtner el usuario"
                  
                  echo "Ruta de SAM CLI:"
                  which sam || echo "SAM no está en el PATH"
                  
                  echo "Probando versión de SAM:"
                  sam --version || echo "SAM no funciona aquí"
                  
                  echo "Construyendo el paquete SAM..."
                  sam build

                  echo "Validando la plantilla SAM..."
                  sam validate --region us-east-1

                  echo "Desplegando recursos a serverlees al entorno de Staging..."
                  sam deploy --no-fail-on-empty-changeset --parameter-overrides Stage=$STAGE
             '''
            }
        }
        
        stage('Rest Test') {
            steps {
               sh '''
                  echo "Ejecutando pruebas de integración REST solo LECTURA (GET)..."
                  
                  mkdir -p test-reports
                  
                  docker run --rm \
                    -e BASE_URL="$BASE_URL_PROD" \
                    -v "$WORKSPACE:/app" \
                    melissa15/python-pytest:1.0 \
                   -v test/integration/todoApiTest.py \
                   --junitxml=/app/test-reports/pytest-report.xml
             '''
             
             junit 'test-reports/pytest-report.xml'
            
            }
        }

        
        stage('Promote') {
          steps {
          
            withCredentials([usernamePassword(
               credentialsId: 'GITHUB_CREDENTIALS_MELI', 
               usernameVariable: 'GIT_USER', 
               passwordVariable: 'GIT_PASS')]) {
             
             sh  '''
               echo "Promoviendo release..."
               git config user.name "jenkins"
               git config user.email "jenkins@localhost"
               
               echo "Descartando cambios locales..."
               git reset --hard HEAD
               
               git checkout master
               git checkout origin/develop -- test-reports/release.txt || echo "Nada que copiar"
              
              
               git add test-reports/release.txt || echo "Nada que agregar"
               git commit -m "chore(release): versión marcada como release por jenkins" || echo "Nada que commitear"
               
               echo "Pusheando a master..."
               git push https://${GIT_USER}:${GIT_PASS}@github.com/MelissaMelendez15/todo-list-aws-meli.git master
            
            '''
            }
            
          }
        }
        
    }
    
    post {
       always {
           cleanWs()
       }
    }

}
