#!groovy

pipeline {
  agent {
    docker {
      image 'mhhoban/pythonbuild'
      args '-v /var/run/docker.sock:/var/run/docker.sock:rw'
    }
  }
  stages {
    stage('Get Source') {
      steps {
        checkout scm
      }
    }
    stage('Build Docker Image') {
      steps {
        sh './build_docker_image.sh'
        sh 'docker tag mhhoban/dukedoms-card-broker-tests:latest \
          mhhoban/dukedoms-card-broker-tests:$GIT_COMMIT '
      }
    }
    stage('Publish Image to DockerHub') {
      steps {
      withCredentials([[$class: 'UsernamePasswordMultiBinding', credentialsId: 'dockerhub-auth',
                    usernameVariable: 'USERNAME', passwordVariable: 'PASSWORD']]) {
        sh 'docker login -u $USERNAME -p $PASSWORD && \
          docker push mhhoban/dukedoms-card-broker-tests:latest && \
          docker push mhhoban/dukedoms-card-broker-tests:$GIT_COMMIT'

      }
    }
  }
  }
  post {
    always {
      cleanWs()
    }
  }

}
