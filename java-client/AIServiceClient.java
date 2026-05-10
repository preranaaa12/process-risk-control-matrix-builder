package com.internship.tool.client;

import org.springframework.http.HttpEntity;
import org.springframework.http.HttpHeaders;
import org.springframework.http.MediaType;
import org.springframework.http.ResponseEntity;
import org.springframework.stereotype.Component;
import org.springframework.web.client.RestTemplate;
import org.springframework.web.client.RestClientException;
import org.springframework.boot.web.client.RestTemplateBuilder;

import java.time.Duration;
import java.util.Map;
import java.util.HashMap;

@Component
public class AIServiceClient {

    private final RestTemplate restTemplate;
    private final String baseUrl = "http://localhost:5000";

    public AIServiceClient(RestTemplateBuilder builder) {
        this.restTemplate = builder
                .setConnectTimeout(Duration.ofSeconds(10))
                .setReadTimeout(Duration.ofSeconds(10))
                .build();
    }

    private Map<String, Object> callEndpoint(String path, String text) {
        try {
            HttpHeaders headers = new HttpHeaders();
            headers.setContentType(MediaType.APPLICATION_JSON);
            
            Map<String, String> requestBody = new HashMap<>();
            requestBody.put("text", text);
            
            HttpEntity<Map<String, String>> request = new HttpEntity<>(requestBody, headers);
            
            ResponseEntity<Map> response = restTemplate.postForEntity(baseUrl + path, request, Map.class);
            return response.getBody();
        } catch (RestClientException e) {
            return null;
        }
    }

    public Map<String, Object> describe(String text) {
        return callEndpoint("/describe", text);
    }

    public Map<String, Object> recommend(String text) {
        return callEndpoint("/recommend", text);
    }

    public Map<String, Object> generateReport(String text) {
        return callEndpoint("/generate-report", text);
    }
}
