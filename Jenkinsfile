pipeline {
  agent any
  stages {
    stage('Build') {
      parallel {
        stage('Build') {
          agent any
          steps {
            sh 'docker --version'
          }
        }

        stage('Build Docker Image') {
          agent any
          steps {
            echo 'create docker image'
            sh 'cd apps'
            sh 'docker build --tag python-poc-cicd:latest .'
          }
        }

      }
    }

  }
}