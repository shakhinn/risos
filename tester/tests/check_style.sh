CYAN='\033[0;36m'
NC='\033[0m' # No Color

TESTS_FOLDER='/devops-examples/EXAMPLE_APP/tests'

# Create folder if not exist
mkdir -p ${TESTS_FOLDER}/test_results;

  echo -e "${CYAN}CODE STYLE TESTS${NC}";
  # run yapf style tests
  pep8 --first --statistics --count . \
   > >(tee /var/log/style-tests.log /proc/1/fd/1) 2> >(tee /var/log/style-tests.err /proc/1/fd/2)