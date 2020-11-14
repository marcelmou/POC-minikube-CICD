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

    stage('Test') {
      parallel {
        stage('Test') {
          steps {
            echo 'Starting test for new build'
          }
        }

        stage('start container (new image)') {
          steps {
            sh 'docker run -d -p 8081:5000 --name python-poc-cicd python-poc-cicd:latest'
          }
        }

        stage('test http connection') {
          steps {
            sh 'curl http://localhost:8081'
          }
        }

        stage('kill container') {
          steps {
            sh 'docker kill python-poc-cicd && docker container rm python-poc-cicd'
          }
        }

      }
    }

  }
}