#!/usr/bin/env bash

set -o errexit
set -o errtrace
set -o nounset
set -o pipefail
if [[ ! -z ${DEBUG_MODE+x} ]]; then
    set -o xtrace
    set -o functrace
fi

BASE_DIR="$(cd "$(dirname "${BASH_SOURCE[-1]}")" && pwd)"
BUILD_DIR="$BASE_DIR/build"

# TODO: Exclude .DS_Store

aws s3 sync --exclude .DS_Store --profile familycodex "$BUILD_DIR" s3://www.familycodex.net/
