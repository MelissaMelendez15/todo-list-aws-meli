pipeline { 
   agent any 
   
   environment {
       GITHUB_CREDENTIALS_MELI = credentials('GITHUB_CREDENTIALS_MELI')
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
                  sam deploy --no-fail-on-empty-changeset --parameter-overrides Stage =$STAGE
               '''
            }
         }
      }
   }
