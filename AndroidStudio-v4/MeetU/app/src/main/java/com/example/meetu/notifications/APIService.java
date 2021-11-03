package com.example.meetu.notifications;

import retrofit2.Call;
import retrofit2.http.Body;
import retrofit2.http.Headers;
import retrofit2.http.POST;

public interface APIService {

    @Headers({
            "Content-Type:application/json",
            "Authorization:key=AAAA5YOPT5U:APA91bGtMho_8iWmNwJygfPq51OhSYgTmzRuFGjwx-VQuh7ni2rvzSsQJkI2ijGdpFxpQfpQbw1-kO3OqR11oEpm_LyTxeVbmUs4dsfhjrqeXnsNseMcef39mhS0bJTfiIQV3KCGv_8r\t\n"
    })

    @POST("fcm/send")
    Call<Response> sendNotification(@Body Sender body);
}
