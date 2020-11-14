pipeline {
  agent {
    dockerfile {
      filename 'DockerFile'
    }

  }
  stages {
    stage('Build') {
      agent any
      steps {
        sh 'docker --version'
      }
    }

  }
}