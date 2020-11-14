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
            sh 'ls -al'
            sh 'docker build --tag python-poc-cicd:latest .'
          }
        }

      }
    }

  }
}