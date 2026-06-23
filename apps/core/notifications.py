"""Form bildirimleri.

Şimdilik formlar yalnızca DB'ye kaydedilir. EMAIL_ENABLED=True olduğunda
(profesyonel hosting'e geçişte) bu fonksiyon bildirim e-postası gönderir —
çağıran view kodu değişmeden çalışmaya devam eder.
"""

from django.conf import settings
from django.core.mail import send_mail


def notify_submission(subject: str, message: str) -> None:
    """Yeni form gönderimi için bildirim e-postası (etkinse) gönder."""
    if not settings.EMAIL_ENABLED or not settings.CONTACT_NOTIFY_EMAIL:
        return
    send_mail(
        subject=subject,
        message=message,
        from_email=settings.DEFAULT_FROM_EMAIL or None,
        recipient_list=[settings.CONTACT_NOTIFY_EMAIL],
        fail_silently=True,
    )
