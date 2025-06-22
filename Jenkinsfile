pipeline {

    agent any 
    
    
    evironment {
       GITHUB_TOKEN1 = credentials('GITHUB_TOKEN1')
    }

    
    stages {
    
       stage('Get Code') {
           steps {
              git branch: 'develop',
                  url: "https://${GITHUB_TOKEN1}@github.com/MelissaMelendez15/todo-list-aws-meli.git"
           
           }
       
       }
       
       stage('validar entorno') {
          steps {
            echo "Pipeline funcionando correctamente"
          }
       }
    
    }



}
