pipeline {

    agent any 
    
    
    evironment {
       GITHUB_TOKEN = credentials('GITHUB_TOKEN')
    }

    
    stages {
    
       stage('Get Code') {
           steps {
              git branch: 'develop',
                  url: "https://${GITHUB_TOKEN}@github.com/MelissaMelendez15/todo-list-aws-meli.git"
           
           }
       
       }
       
       stage('validar en') {
          steps {
            echo "Pipeline funcionando correctamente"
          }
       }
    
    }



}
