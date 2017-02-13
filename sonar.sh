
die () 
{
    echo >&2 "$@"
    exit 1
}

[ "$#" -eq 1 ] || die "1 argument required, $# provided"

cd $1
echo "Compiling $1"
mvn clean compile test-compile

echo "Launching unitary tests"
mvn -Plocalhost test sonar:sonar

