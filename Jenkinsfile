pipeline {

    agent any 
    
    
    environment {
       GITHUB_CREDENTIALS_MELI = credentials('GITHUB_CREDENTIALS_MELI')
    }

    
    stages {
    
       stage('Get Code') {
           steps {
              git branch: 'develop',
                  url: "https://${GITHUB_CREDENTIALS_MELI}@github.com/MelissaMelendez15/todo-list-aws-meli.git"
           
           }
       
       }
       
       stage('validar entorno') {
          steps {
            echo "Pipeline funcionando correctamente"
          }
       }
    
    }



}
