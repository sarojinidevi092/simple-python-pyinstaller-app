pipeline {
  agent any
  stages {
    stage('Build') {
      agent {
        docker {
           image 'python:2-alpine'
        }
      }
      steps {
        sh 'python -n py_compile sources/add2vals.py sources/calc.py'
        stash(name: 'compiled-results', includes: 'sources/*.py*')
      }
    }
  }
} 
    