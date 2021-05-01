/**
 * 文字列が空文字かチェックする
 * @param {チェック対象文字列}} _str
 * @returns {true 空文字, false not 入力有}
 */
function commonCheckStrIsEmpty(_str) {
  if (commonCheckIsNull(_str)) {
    return true;
  }
  if (_str === "") {
    return true;
  }

  return false;
}

/**
 * パラメータがJson形式チェックする
 * @param {バリュー} value
 */
function commonCheckFormatJson(value) {
  if (commonCheckIsNull(value)) {
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
 * @returns {true null, false not null}
 */
function commonCheckIsNull(value) {
  if (value === null) {
    return true;
  }

  if (undefined === typeof value) {
    return true;
  }

  return false;
}
