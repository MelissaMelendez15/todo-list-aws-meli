pipeline { 
   agent any 
   
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
               echo "Descargando configuración desde repo externo (production)..."
               curl -o samconfig.toml https://raw.githubusercontent.com/MelissaMelendez15/todo-list-aws-config/production/samconfig.toml
            
               echo "Contenido del samconfig.toml descargado:"
               ls -l samconfig.*
               cat samconfig.toml
            '''
            
          }
        }
        
        stage('Deploy') {
            steps {
               sh '''
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

                  echo "Desplegando recursos a serverlees al entorno de PRODUCCIÓN..."
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
                      -v test/integration/todoApiReadOnlyTest.py \
                      --junitxml=/app/test-reports/pytest-report.xml
                 '''
                 
                 junit 'test-reports/pytest-report.xml'
            }
         }
      }
      
      post {
         always {
             cleanWs()
         }
      }
   }
