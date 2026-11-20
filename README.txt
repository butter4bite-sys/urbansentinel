URBAN SENTINEL — GEMINI ASSISTANT

1. Copy assistant.html, assets/js/gemini-assistant.js, and netlify/functions/chat.js into your existing website, keeping folders intact.
2. In Netlify > Site configuration > Environment variables, add GEMINI_API_KEY with your NEW Gemini API key. Do not place the key in HTML/JavaScript or commit it to Git.
3. Set the variable scope to Functions (or all scopes) and redeploy the site.
4. Ensure Netlify Functions are enabled and the site is deployed from the folder containing netlify/functions.
5. Open assistant.html on the deployed website and try a question.

IMPORTANT SECURITY: Since an API key was pasted into chat, revoke/rotate that key and use a newly generated one. A normal Google Gemini API key generally starts with AIza; verify your key is a Gemini API key from Google AI Studio.

This integration has no hardcoded API key. The function uses the Gemini API (subject to Google free-tier limits and rate limits). No payment is required if usage stays within available free-tier allowances. Public users can consume your quota; add rate limiting or access controls before broad launch.

The saved-project selector remains in the page, but the actual project data is not passed unless you integrate your existing project's storage format. Only the selected option label is currently included.

SCOPE: Gemini is now instructed server-side to answer Urban Sentinel, urban planning, environment, AQI, temperature, drainage, sustainability, budgets, and related science questions. Unrelated topics should receive a brief refusal. This is prompt-based scoping, not a guaranteed hard security boundary; add server-side classification and rate limiting if stronger enforcement is needed.
