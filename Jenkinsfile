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
            sh 'docker build --tag moukkelchen/python-poc-cicd:test .'
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

        stage('start and test new image') {
          steps {
            sh 'docker run -d -p 8081:5000 --name python-poc-cicd moukkelchen/python-poc-cicd:test'
            echo 'waiting 10sec for coming up'
            sleep 10
            sh 'docker kill python-poc-cicd && docker container rm python-poc-cicd'
          }
        }

      }
    }

    stage('Deploy') {
      parallel {
        stage('Deploy') {
          steps {
            echo 'start deploy process'
          }
        }

        stage('Release to DockerHub') {
          steps {
            sh 'docker tag moukkelchen/python-poc-cicd:test moukkelchen/python-poc-cicd:latest'
            sh 'docker push moukkelchen/python-poc-cicd:latest'
          }
        }

      }
    }

  }
}