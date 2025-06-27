pipeline { 
   agent any 
   
   enviroment {
       GITHUB_CREDENTIALS_MELI = credentials('GITHUB_CREDENTIALS_MELI')
   }
   
   stages {
      stage('Get Code'){
        // Etapa Get Code
          steps {
             git branch: 'master'
                 url: "https://${GITHUB_CREDENTIALS_MELI}@github.com/MelissaMelendez15/todo-list-aws-meli.git"
             
             sh '''
                echo "Clonando configuración de producción..."
                git clone --branch production https://github.com/MelissaMelendez15/todo-list-aws-config.git config-repo
                cp config-repo/samconfig.toml .
             '''
          }
        } 
    }

}
