pipeline {

    agent any
      docker {
        image 'python:3.10'
        args '-v /var/run/docker.sock:/var/run/docker.sock'
    }
    
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
       
       stage('Static') {
          steps {
             sh  '''
                 pip install flake8 bandit
                 echo "Ejecutando Flake8..."
                 flake8 src/ --exit-zero --format=default > flake8-report.txt || true
                 
                 echo "Ejecutando Bandit..."
                 bandit -r src/ -f txt -o bandit-report.txt || true
             '''
             
             recordIssues tools: [flake8(pattern: 'flake8-report.txt')]
    
            }
       }
    
    }



}
