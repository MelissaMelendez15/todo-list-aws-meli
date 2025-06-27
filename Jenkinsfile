pipeline { 
   agent any 
   
   environment {
       GITHUB_CREDENTIALS_MELI = credentials('GITHUB_CREDENTIALS_MELI')
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
                echo "Descargando samconfig.toml desde rama production..."
                git fetch origin production
                git show origin/production:samconfig.toml  > samconfig.toml
             '''
          }
        } 
    }

}
