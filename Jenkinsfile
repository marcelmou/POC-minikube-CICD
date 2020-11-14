pipeline {
  agent {
    dockerfile {
      filename 'app/DockerFile'
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