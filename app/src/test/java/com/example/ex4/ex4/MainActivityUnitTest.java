package com.example.ex4.ex4;

import android.text.Editable;
import android.text.SpannableStringBuilder;
import android.widget.EditText;

import org.junit.Test;
import org.junit.runner.RunWith;
import org.mockito.Mock;
import org.mockito.runners.MockitoJUnitRunner;

import java.util.ArrayList;

import static org.junit.Assert.*;
import static org.mockito.Mockito.mock;
import static org.mockito.Mockito.when;

@RunWith(MockitoJUnitRunner.class)
public class MainActivityUnitTest {
    private static final String FAKE_USERNAME = "a";
    private static final String FAKE_PASSWORD = "fake_password";

    @Mock
    EditText username;
    @Mock
    EditText password;

    @Test
    public void MainActivity_authenticateLogin1() throws Exception {
        // users is null
        MainActivity m = new MainActivity();
        Editable u = mock(SpannableStringBuilder.class);
        when(u.toString()).thenReturn(FAKE_USERNAME);
        Editable p = mock(SpannableStringBuilder.class);
        when(p.toString()).thenReturn(FAKE_PASSWORD);
        when(username.getText()).thenReturn(u);
        when(password.getText()).thenReturn(p);
        m.setUsernameBox(username);
        m.setPasswordBox(password);
        boolean res = m.authenticateLogin(null);
        assertEquals(res, false);
    }
    @Test
    public void MainActivity_authenticateLogin2() throws Exception {
        // right username wrong password
        MainActivity m = new MainActivity();
        m.users = new ArrayList<>();
        User user = new User();
        user.username = FAKE_USERNAME;
        user.password = FAKE_PASSWORD+"a";
        Editable u = new SpannableStringBuilder(FAKE_USERNAME);
        Editable p = new SpannableStringBuilder(FAKE_PASSWORD);
        when(username.getText()).thenReturn(u);
        when(password.getText()).thenReturn(p);
        m.setUsernameBox(username);
        m.setPasswordBox(password);
        //boolean res = m.authenticateLogin(null);
        //assertNotEquals(m.users, null);
        //assertEquals(res, false);
    }
}