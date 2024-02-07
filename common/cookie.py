# -*- coding: utf-8 -*-
import org.apache.http.HttpEntity;
import org.apache.http.client.ClientProtocolException;
import org.apache.http.client.CookieStore;
import org.apache.http.client.methods.CloseableHttpResponse;
import org.apache.http.client.methods.HttpGet;
import org.apache.http.cookie.Cookie;
import org.apache.http.impl.client.BasicCookieStore;
import org.apache.http.impl.client.CloseableHttpClient;
import org.apache.http.impl.client.HttpClients;
import org.apache.http.util.EntityUtils;
import com.alibaba.fastjson.JSONObject;

String dpa_analysis_cookie = null;

CloseableHttpClient httpClient = null;
        HttpGet httpGet = null;
        String data;
        httpClient = HttpClients.createDefault();
        CookieStore cookieStore = new BasicCookieStore();
        httpClient = HttpClients.custom().setDefaultCookieStore(cookieStore).build();
        httpGet = new HttpGet("https://analysis-api.test.ztosys.com/api/user/info");
        httpGet.setHeader("X-Canvas-Fingerprint","c47dbb60a90e7dbb158c8ccb76b11772");
        httpGet.setHeader("Authorization","Secret MCfYk0FtptSVvMZfEqkV+kEeh7uFVTmF0dWHujVJGJzQTLdikaSQVNhK52pIV2pYysd8sC/aqwcsKH2RQFjOc9CgDLUeSfrXeXcXNIg1q1d5WphU3EViTeFfCvR2997WmCsgHgt2GhBKM4N137oDXIPoPMlGHw1MQ6NfUlYyPruKXGwOUqhIkPRJ3kFSeaIzfL0tSZNSlwjfI+mvylMqSXvnsAW/Z7BYpyuRVQJT5sq0Eh9anQ+IgbmaLpgmu57/P+zPKeEQSfQK3i3kD0smPXHLtsGguJUAjdsOzSubhQQ0H0P6Ts4s6reEdcYMUpz/MLwOznVtckRFJ5eOYPKwVw==");
        httpGet.setHeader("User-Agent","Chrome%20PDF%20Plugin%3A%3APortable%20Document%20Format%3A%3Aapplication%2Fx-google-chrome-pdf~pdf%3BChrome%20PDF%20Viewer%3A%3A%3A%3Aapplication%2Fpdf~pdf%3BNative%20Client%3A%3A%3A%3Aapplication%2Fx-nacl~%2Capplication%2Fx-pnacl");
        httpGet.setHeader("Content-Type","application/json");
        CloseableHttpResponse response = httpClient.execute(httpGet);
        HttpEntity httpEntity = response.getEntity();
        // 接口响应结果
        data = EntityUtils.toString(httpEntity, "utf-8");
        JSONObject object = JSONObject.parseObject(data);
	   log.info("1################=" + object);
        String url = object.getString("redirect_uri");
	   log.info("2################=" + url);
        httpGet = new HttpGet(url);
        response = httpClient.execute(httpGet);
        // 获取cookies信息
//        List<Cookie> cookieList = cookieStore.getCookies();
        List cookieList = cookieStore.getCookies();
//        Map map = new HashMap<>();
        Map map = new HashMap();
        for (Cookie cookie : cookieList){
          if(cookie.getName().equals("SESSION")){
			dpa_analysis_cookie = cookie.getValue();
//          map.put("cookie","SESSION="+cookie.getValue());

          }
        }
        if(null != response){
        	response.close();
        }
        if(null != httpClient){
        	httpClient.close();
        }

//
log.info("SESSION=" + dpa_analysis_cookie);
vars.put("dpa_analysis_cookie","SESSION=" + dpa_analysis_cookie);