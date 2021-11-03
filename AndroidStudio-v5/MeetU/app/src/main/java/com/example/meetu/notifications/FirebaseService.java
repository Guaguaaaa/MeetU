package com.example.meetu.notifications;

import com.google.firebase.auth.FirebaseAuth;
import com.google.firebase.auth.FirebaseUser;
import com.google.firebase.database.DatabaseReference;
import com.google.firebase.database.FirebaseDatabase;
import com.google.firebase.installations.FirebaseInstallations;
import com.google.firebase.messaging.FirebaseMessagingService;

public class FirebaseService extends FirebaseMessagingService {

    @Override
    public void onNewToken(String mToken){
        super.onNewToken(mToken);
        FirebaseUser user = FirebaseAuth.getInstance().getCurrentUser();
        //String newToken = FirebaseInstallations.getInstance().getToken();
        if (user != null){
            updateToken(mToken);
        }
    }

    private void updateToken(String mToken) {
        FirebaseUser user = FirebaseAuth.getInstance().getCurrentUser();
        DatabaseReference ref = FirebaseDatabase.getInstance().getReference("Tokens");
        Token token = new Token(mToken);
        ref.child(user.getUid()).setValue(token);
    }
}
