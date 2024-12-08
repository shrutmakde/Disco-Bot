pipeline {
    agent any
    environment {
        KUBECONFIG = credentials('kubeconfig-credentials') // Add K8s credentials in Jenkins
    }
    stages {
        stage('Checkout') {
            steps {
                checkout scm
            }
        }
        stage('Build') {
            steps {
                echo 'Building the project...'
                sh 'echo "Build commands go here"'
            }
        }
        stage('Deploy to Kubernetes') {
            steps {
                echo 'Deploying to Kubernetes...'
                sh '''
                kubectl apply -f k8s/deployment.yaml
                kubectl rollout status deployment/my-app
                '''
            }
        }
    }
    post {
        failure {
            mail to: 'shrutmakde6201@gmail.com',
                subject: "Build Failed: ${env.JOB_NAME} ${env.BUILD_NUMBER}",
                body: "Please check the Jenkins console output for more details."
        }
    }
}
