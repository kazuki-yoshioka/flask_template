/**
 * POSTデータ送信
 */
function sendJsonData() {
  //連想配列
  var json_asocc = [
    {
      maker: "MAZDA",
      model: "DEMIO",
      grade: "XD L pakage",
    },
  ];
  url = "http://localhost:5000/fetch";
  //JSONにエンコード
  var JSONdata = JSON.stringify(json_asocc);

  $.ajax({
    type: "post",
    url: url,
    data: JSONdata,
    contentType: "application/JSON",
    dataType: "JSON",
    scriptCharset: "utf-8",
    success: function (data) {
      // Success
      alert("success");
      alert(JSON.stringify(data));
      $("#response").html(JSON.stringify(data));
    },
    error: function (data) {
      // Error
      alert("error");
      alert(JSON.stringify(data));
      $("#response").html(JSON.stringify(data));
    },
  });
}

/**
 * 画面遷移
 * url: 画面遷移するurl
 */
function sendRequestMoveDisplay(_url) {
  window.location.href = location.origin + _url;
}

/**
 * JSONデータを取得する
 * 画面を最新化する
 */
function commonFetchDataRefresh(_param, _url, _successDoneFunc) {
  var url = "";
  if (_param == null || JSON.stringify(_param) === "{}") {
    _param = { none: "none" };
  }
  _param["nextUrl"] = location.origin + "/move";
  if (null == _url) {
    url = location.href;
  } else {
    url = location.origin + "/" + _url;
  }

  fetch(url, {
    method: "POST", // or 'PUT'
    headers: {
      "Content-Type": "application/json",
    },
    body: JSON.stringify(_param),
  })
    .then((response) => response.json())
    .then((data) => {
      console.log("Success:", data);

      // データ取得、後処理を実行
      commonMoveDisplay();
    })
    .catch((error) => {
      console.error("Error:", error);
    });
}
/**
 * JSONデータを取得する
 */
function commonFetchData(_param, _url, _successDoneFunc) {
  var url = "";
  if (_param == null || JSON.stringify(_param) === "{}") {
    _param = { none: "none" };
  }
  if (null == _url) {
    url = location.href;
  } else {
    url = location.origin + "/" + _url;
  }

  fetch(url, {
    method: "POST", // or 'PUT'
    headers: {
      "Content-Type": "application/json",
    },
    body: JSON.stringify(_param),
  })
    .then((response) => response.json())
    .then((data) => {
      console.log("Success:", data);

      // データ取得、後処理を実行
      if (_successDoneFunc && typeof _successDoneFunc === "function") {
        _successDoneFunc(JSON.stringify(data));
      }

      // 次画面URLがセットされている場合、次画面へ遷移
      if (!commonCheckStrIsEmpty(data["nextUrl"])) {
        commonMoveDisplay(data["nextUrl"]);
      }
    })
    .catch((error) => {
      console.error("Error:", error);
    });
}

/**
 * サーバにリクエストを送信する
 * @param {リクエストパラメータ} _param
 * @param {リクエストするパラメータ} _url
 * @param {サーバから返答後の処理} _successDoneFunc
 */
function sendRequestServer(_param, _url, _successDoneFunc) {
  if (!commonCheckFormatJson(_param)) {
    alert("パラメータがJson形式ではありません。");
    return;
  }

  if (!commonCheckStrIsEmpty(_url)) {
    alert("サーバに送信用のUrlが空です。");
    return;
  }

  var url = location.origin + _url;
  fetch(url, {
    method: "POST",
    headers: {
      "Content-Type": "application/json",
    },
    body: JSON.stringify(_param),
  })
    .then((response) => response.json())
    .then((data) => {
      console.log("Success:", data);

      // 次画面URLがセットされている場合、次画面へ遷移
      if (!commonCheckStrIsEmpty(data["nextUrl"])) {
        sendRequestMoveDisplay(data["nextUrl"]);
      }

      // データ取得、後処理を実行
      if (
        commonCheckIsNull(_successDoneFunc) &&
        typeof _successDoneFunc === "function"
      ) {
        _successDoneFunc(JSON.stringify(data));
      }
    })
    .catch((error) => {
      console.error("Error:", error);
    });
}
