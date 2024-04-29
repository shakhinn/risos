
function code_style() {
    echo -e "CODE STYLE TESTS";
    bash tests/check_style.sh 2>&1 | tee -a /proc/1/fd/1 tester-logs.log
}

function integration() {
    echo -e "INTEGRATION TESTS";
    pytest tests/integration.py 2>&1 | tee -a /proc/1/fd/1 tester-logs.log
}


code_style
integration
