#!/usr/bin/env bash

set -o errexit
set -o errtrace
set -o nounset
set -o pipefail
if [[ ! -z ${DEBUG_MODE+x} ]]; then
    set -o xtrace
    set -o functrace
fi

DIR="$( cd "$( dirname "${BASH_SOURCE[0]}" )" && pwd )";
BASE_DIR="${DIR%/*}"
BUILD_DIR="$BASE_DIR/build"
MEDIA_DIR="$BASE_DIR/media"

# Nuke any .DS_Store files before syncing.
find "$BASE_DIR" -name "*.DS_Store" -delete

# Sync the media directory
if [[ -d "$MEDIA_DIR" ]]; then
    aws s3 sync --profile familycodex "$MEDIA_DIR" s3://www.familycodex.net/media
else
    echo "$MEDIA_DIR does not exist, not uploading any new media."
fi

# Sync the build directory
if [[ -d "$BUILD_DIR" ]]; then
    aws s3 sync --profile familycodex "$BUILD_DIR" s3://www.familycodex.net/
else
    echo "$BUILD_DIR does not exist, cannot upload site code."
fi
