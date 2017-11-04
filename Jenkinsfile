pipeline {
  agent any
  stages {
    stage('1') {
      steps {
        sleep 30
        echo 'Hello Step 1'
        sh 'echo koko >> /tmp/jenkins.txt'
      }
    }
    stage('2') {
      steps {
        sh 'cat /tmp/jenkins.txt'
      }
    }
  }
}