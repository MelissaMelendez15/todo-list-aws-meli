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
                echo "El archivo samconfig.toml ya está presente en la rama master"
             '''
          }
        } 
    }

}
