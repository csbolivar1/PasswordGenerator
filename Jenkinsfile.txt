stages {
	stage('Build') {
		steps {
			echo 'Building...'
			python PasswordGenerator.py
		}
	}
}