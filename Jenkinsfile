pipeline
{
    agent any
    stages
  {
	  stage('checkout')
	  {
		  checkout([$class: 'GitSCM', branches: [[name: '*/master']], extensions: [], userRemoteConfigs: [[url: 'https://github.com/16641A0575/manasa.git']]])
	  }
	  stage('static code analysis')
	  {
		  echo "static code analysis"
	  }
	  stage('Build')
	  {
		  echo "build the code"
	  }
	  stage('unit testing')
	  {
		  echo "unit testing"
	  }
	  stage('delivery')
	  {
		  echo "delivery"
	  }
	post
  {
		failure
		{
			emailext body: 'fail', subject: 'pipeline status', to: 'dhadimsnasa@gmail.com'
		}
		success
		{
			emailext body: 'pass', subject: 'pipeline status', to: 'dhadimsnasa@gmail.com'
		}
	}
  }
}
