/**
 * 文字列が空文字かチェックする
 * @param {チェック対象文字列}} _str
 * @returns
 */
function commonCheckStrIsEmpty(_str) {
  if (!commonCheckIsNull(_str)) {
    return false;
  }
  if (_str === "") {
    return false;
  }

  return true;
}

/**
 * パラメータがJson形式チェックする
 * @param {バリュー} value
 */
function commonCheckFormatJson(value) {
  if (!commonCheckIsNull(value)) {
    return false;
  }
  if (JSON.stringify(value) === {}) {
    return false;
  }
  return true;
}

/**
 * nullチェック
 * @param {バリュー} value
 */
function commonCheckIsNull(value) {
  if (value === null) {
    return false;
  }

  if (undefined === typeof value) {
    return false;
  }

  return true;
}
