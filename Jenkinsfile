pipeline
{
    agent any
    stages
  {
	  stage('checkout')
	  {
	  	steps
	   	{
		  	checkout([$class: 'GitSCM', branches: [[name: '*/master']], extensions: [], userRemoteConfigs: [[url: 'https://github.com/16641A0575/manasa.git']]])
	   	}
	  }
	  stage('static code analysis')
	  {
		  steps
		  {
		  	echo "static code analysis"
		  }
	  }
	  stage('Build')
	  {
		  steps
		  {
		  	echo "build the code"
		  }
	  }
	  stage('unit testing')
	  {
		  steps
		  {
		  	echo "unit testing"
		  }
	  }
	  stage('delivery')
	  {
		  steps
		  {
		  	echo "delivery"
		  }
	  }
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

