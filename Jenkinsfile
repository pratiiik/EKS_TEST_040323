pipeline {
    agent any


    stages {
        stage('clone') {
            steps {
                // Get some code from a GitHub repository
                git 'https://github.com/pratiiik/EKS_TEST_040323.git'

                // Run Maven on a Unix agent.
                // sh "mvn -Dmaven.test.failure.ignore=true clean package"

                // To run Maven on a Windows agent, use
                // bat "mvn -Dmaven.test.failure.ignore=true clean package"
            }

            post {
                // If Maven was able to run the tests, even if some of the test
                // failed, record the test results and archive the jar file.
                success {
                //    junit '**/target/surefire-reports/TEST-*.xml'
                //    archiveArtifacts 'target/*.jar'
                sh "echo 'executed script to clone'"
                }
            }
        }
        stage('docker image build') {
            steps {
                script {
                    app = docker.build("python-app")
                }
            }
            post {
                
                success {
                sh "echo 'Docker image building done'"
                }
            }
        }
        stage('docker image push to ECR') {
            steps {
                script {
                    docker.withRegistry('https://018556395605.dkr.ecr.ap-northeast-1.amazonaws.com', 'ecr:ap-northeast-1:aws-credential'){
                        app.push("${env.BUILD_NUMBER}")
                        app.push("latest")
                    }
                }
            }
            post {
                
                success {
                sh "aws ecr describe-images --repository-name python-app --image-ids imageTag=latest --output text"
                sh "echo 'Docker image pushed to ECR'"
                }
            }
        }
        
    }
}
