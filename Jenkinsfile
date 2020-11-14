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
          agent {
            dockerfile {
              filename 'apps/DockerFile'
            }

          }
          steps {
            echo 'create docker image'
          }
        }

      }
    }

  }
}