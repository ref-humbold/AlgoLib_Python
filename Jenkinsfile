pipeline {
  agent {
    label "local"
  }

  parameters {
    booleanParam(name: "sphinx", description: "Should generate Sphinx documentation?", defaultValue: false)
  }

  environment {
    VENV_DIR = ".venv"
    TEST_RESULT = "nose2-junit.xml"
    PYLINT_RESULT = "pylint.log"
  }

  options {
    skipDefaultCheckout(true)
    timeout(time: 20, unit: "MINUTES")
    buildDiscarder(logRotator(numToKeepStr: "10", artifactNumToKeepStr: "5"))
    timestamps()
  }

  stages {
    stage("Preparation") {
      steps {
        script {
          def scmEnv = checkout(scm)
          currentBuild.displayName = "${env.BUILD_NUMBER} ${scmEnv.GIT_COMMIT.take(8)}"
        }
      }
    }

    stage("Install packages") {
      steps {
        echo "#INFO: Installing PIP packages"
        sh """
          set +x
          python3 -m virtualenv ${env.VENV_DIR}
          . ${env.VENV_DIR}/bin/activate

          pip install -r requirements.txt
          pip install -r requirements.dev.txt

          deactivate
        """
      }
    }

    stage("Unit tests") {
      steps {
        echo "#INFO: Running unit tests"
        sh """
          set +x
          . ${env.VENV_DIR}/bin/activate

          nose2 tests
          sed -i -r 's/timestamp="[^"]+"//g' ${env.TEST_RESULT}

          deactivate
        """
      }

      post {
        always {
          xunit(
            tools: [JUnit(
              pattern: "${env.TEST_RESULT}",
              failIfNotNew: true,
              stopProcessingIfError: true
            )],
            thresholds: [failed(unstableThreshold: "0", failureThreshold: "0")]
          )
        }
      }
    }

    stage("PyLint") {
      steps {
        echo "#INFO: Running PyLint"
        sh """
          set +x
          . ${env.VENV_DIR}/bin/activate

          pylint --exit-zero --rcfile=pylintrc algolib tests > ${env.PYLINT_RESULT}

          deactivate
        """
      }

      post {
        always {
          recordIssues(tool: pyLint(pattern: "${env.PYLINT_RESULT}"))
        }
      }
    }

    stage("Sphinx documentation") {
      when {
        beforeAgent true
        expression {
          params.sphinx
        }
      }

      steps {
        echo "#INFO: Publish Sphinx documentation"
        sh """
          set +x
          . ${env.VENV_DIR}/bin/activate

          sh docs/docs.sh

          deactivate
        """
      }
    }
  }

  post {
    always {
      chuckNorris()
    }

    cleanup {
      cleanWs()
    }
  }
}
