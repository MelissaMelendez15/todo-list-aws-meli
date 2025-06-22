pipeline {

    agent {
      docker {
        image 'melissa15/python-static-checker:1.0'
        reuseNode true
      }
    
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
                 echo "Ejecutando Flake8..."
                 flake8 src/ --exit-zero --format=default > flake8-report.txt || true
                 
                 echo "Ejecutando Bandit..."
                 bandit -r src/ -f txt -o bandit-report.txt || true
             '''
             
             recordIssues tools: [flake8(pattern: 'flake8-report.txt')]
             recordIssues tools: [bandit(pattern: 'bandit-report.txt')]
    
            }
        }
    
    
    }



}
