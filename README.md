# Orlantech Nexus Feedback Module
A plug-and-play, asynchronous feedback system designed for Django projects. 

### Key Features:
* **Standalone Architecture**: Can be imported into any Django project without modifying core logic.
* **AJAX Powered**: Submits feedback without page reloads, preserving user session state.
* **Device Aware**: Automatically captures User-Agent data to debug mobile UI collisions and notch-overlap issues.
* **Amber-500 Aesthetic**: Styled to match the Orlantech Innovations / Ironclad branding.

### Integration:
1. Add `orlantech_feedback` to `INSTALLED_APPS`.
2. Include `path('nexus/', include('orlantech_feedback.urls'))` in main `urls.py`.
3. Add `{% include 'orlantech_feedback/feedback_component.html' %}` to `base.html`.   #incase u encunter template load issues ,add just before the close of the body tag 