pipeline {

    agent any
      
    environment {
       GITHUB_CREDENTIALS_MELI = credentials('GITHUB_CREDENTIALS_MELI')
       BASE_URL_PROD = credentials('BASE_URL_PROD')
    }

    stages {
    
       stage('Get Code') {
           steps {
              git branch: 'develop',
                  url: "https://${GITHUB_CREDENTIALS_MELI}@github.com/MelissaMelendez15/todo-list-aws-meli.git"
           
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
                  sam deploy --no-fail-on-empty-changeset
             '''
            }
        }
        
        stage('Rest Test') {
          steps {
             sh  '''
                  echo "Ejecutando pruebas de integración REST..."
                  
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

    
    }



}
