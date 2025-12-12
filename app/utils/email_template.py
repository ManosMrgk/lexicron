from datetime import datetime
from html import escape

def build_wotd_newsletter_body(word: str, uri: str) -> str:
    """
    Professional HTML email body for a Greek Word of the Day newsletter.
    """
    current_year = datetime.now().year
    safe_word = escape(word or "")
    safe_uri = escape(uri or "", quote=True)

    preheader = f"Η λέξη της ημέρας είναι «{safe_word}». Δες σημασία, χρήση και παραδείγματα."

    html = f"""\
<!doctype html>
<html lang="el">
<head>
  <meta charset="utf-8">
  <meta name="viewport" content="width=device-width, initial-scale=1">
  <meta name="x-apple-disable-message-reformatting">
  <title>Lexicron — Λέξη της Ημέρας</title>
</head>

<body style="margin:0; padding:0; background:#f3f6fb; -webkit-text-size-adjust:100%; -ms-text-size-adjust:100%; font-family: 'Segoe UI', -apple-system, BlinkMacSystemFont, 'Helvetica Neue', Arial, sans-serif;">
  <!-- Preheader (hidden) -->
  <div style="display:none; font-size:1px; line-height:1px; max-height:0px; max-width:0px; opacity:0; overflow:hidden; mso-hide:all;">
    {preheader}
  </div>

  <table role="presentation" width="100%" cellpadding="0" cellspacing="0" border="0" style="background:#f3f6fb;">
    <tr>
      <td align="center" style="padding:28px 16px;">

        <!-- Container -->
        <table role="presentation" width="600" cellpadding="0" cellspacing="0" border="0"
               style="width:600px; max-width:600px; background:#ffffff; border-radius:18px; overflow:hidden; box-shadow:0 10px 30px rgba(16,24,40,0.08);">

          <!-- Header -->
          <tr>
            <td style="padding:0;">

                <!--[if mso]>
                <v:rect xmlns:v="urn:schemas-microsoft-com:vml" fill="true" stroke="false"
                style="width:600px;height:160px;">
                <v:fill type="gradient" angle="135" color="#1d4ed8" color2="#0ea5e9" />
                <v:textbox inset="0,0,0,0">
                <![endif]-->

                <table role="presentation" width="100%" cellpadding="0" cellspacing="0" border="0">
                <tr>
                    <td bgcolor="#2563eb"
                        style="padding:34px 34px 26px 34px;
                            background:#2563eb;
                            background-image:linear-gradient(135deg,#1d4ed8 0%, #2563eb 45%, #0ea5e9 100%);
                            background-repeat:no-repeat;
                            background-size:cover;">
                    <div style="text-align:left;">
                        <div style="display:inline-block; padding:6px 10px; border-radius:999px; background:rgba(255,255,255,0.16); color:#eaf2ff; font-size:12px; letter-spacing:0.6px; font-weight:600;">
                        Lexicron · Λέξη της Ημέρας
                        </div>
                        <h1 style="margin:14px 0 6px 0; font-size:26px; line-height:1.2; color:#ffffff; font-weight:700;">
                        Καλημέρα 👋
                        </h1>
                        <p style="margin:0; font-size:15px; line-height:1.6; color:rgba(255,255,255,0.92);">
                        Καθαρότερη σκέψη, πιο δυνατή έκφραση, μία λέξη τη μέρα.
                        </p>
                    </div>
                    </td>
                </tr>
                </table>

                <!--[if mso]>
                </v:textbox>
                </v:rect>
                <![endif]-->

            </td>
          </tr>

          <!-- Main -->
          <tr>
            <td style="padding:34px 34px 10px 34px;">
              <!-- Word card -->
              <table role="presentation" width="100%" cellpadding="0" cellspacing="0" border="0"
                     style="border:1px solid #e8eef9; border-radius:16px; background:#fbfdff;">
                <tr>
                  <td style="padding:22px 22px 18px 22px;">
                    <p style="margin:0 0 10px 0; font-size:12px; letter-spacing:1.6px; color:#64748b; font-weight:700; text-transform:uppercase;">
                      Η σημερινή λέξη
                    </p>
                    <h2 style="margin:0; font-size:40px; line-height:1.1; letter-spacing:-0.6px; color:#0f172a; font-weight:800;">
                      {safe_word}
                    </h2>
                    <p style="margin:12px 0 0 0; font-size:15px; line-height:1.7; color:#334155;">
                      Άνοιξε τη σελίδα της λέξης για <strong>σημασία</strong>, <strong>χρήση</strong> και <strong>παραδείγματα</strong>.
                    </p>
                  </td>
                </tr>
              </table>

              <!-- Tip box -->
              <table role="presentation" width="100%" cellpadding="0" cellspacing="0" border="0" style="margin-top:18px;">
                <tr>
                  <td style="padding:16px 18px; border-radius:14px; background:#f1f7ff; border:1px solid #dbeafe;">
                    <p style="margin:0; font-size:14px; line-height:1.7; color:#1e3a8a;">
                      <strong>Μικρή πρόκληση:</strong> Χρησιμοποίησε τη λέξη <span style="font-weight:700;">«{safe_word}»</span> σε μια πρόταση σήμερα.
                      Αν θες, γράψ’ την στο αγαπημένο σου τετράδιο
                    </p>
                  </td>
                </tr>
              </table>

              <!-- CTA -->
              <table role="presentation" width="100%" cellpadding="0" cellspacing="0" border="0" style="margin-top:22px;">
                <tr>
                  <td align="center" style="padding:8px 0 18px 0;">
                    <!-- Bulletproof button -->
                    <table role="presentation" cellpadding="0" cellspacing="0" border="0">
                      <tr>
                        <td bgcolor="#2563eb" style="border-radius:999px;">
                          <a href="{safe_uri}"
                             style="display:inline-block; padding:14px 28px; font-size:15px; font-weight:700; color:#ffffff; text-decoration:none; border-radius:999px;">
                            Δες τη λέξη αναλυτικά →
                          </a>
                        </td>
                      </tr>
                    </table>

                    <p style="margin:14px 0 0 0; font-size:12px; line-height:1.6; color:#64748b;">
                      Αν το κουμπί δεν δουλεύει, άνοιξε αυτόν τον σύνδεσμο:
                      <span style="word-break:break-all; color:#2563eb;">{safe_uri}</span>
                    </p>
                  </td>
                </tr>
              </table>

              <!-- Divider -->
              <div style="height:1px; background:#e8eef9; margin:6px 0 0 0;"></div>
            </td>
          </tr>

          <!-- Footer -->
          <tr>
            <td style="padding:18px 34px 30px 34px;">
              <p style="margin:0; font-size:12px; line-height:1.7; color:#64748b;">
                Λαμβάνεις αυτό το email επειδή είσαι εγγεγραμμένος στο <strong>Lexicron</strong>.
              </p>
              <p style="margin:10px 0 0 0; font-size:11px; color:#94a3b8;">
                © {current_year} Lexicron • Φτιαγμένο με αγάπη για τη γλώσσα
              </p>
            </td>
          </tr>

        </table>
      </td>
    </tr>
  </table>
</body>
</html>
"""
    return html


# Example usage:
if __name__ == "__main__":
    word = "Φιλότιμο"
    uri = "https://example.com/words/filotimo"

    email_body = build_wotd_newsletter_body(word, uri)

    with open("newsletter_preview.html", "w", encoding="utf-8") as f:
        f.write(email_body)

    print("Newsletter created successfully!")
    print(f"Word: {word}")
    print("Preview saved to: newsletter_preview.html")
