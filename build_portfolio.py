import base64

# Read the original image
with open(r'C:\Users\sajja\Desktop\kai_data\kai,.jpeg', 'rb') as f:
    img_data = f.read()
    img_b64 = base64.b64encode(img_data).decode('ascii')

# ============================================================
# COMPLETE PORTFOLIO — Tayyaba Sajjad
# Biomedical Engineer × AI/ML Engineer
# ============================================================

html = f'''<!DOCTYPE html>
<html lang="en">
<head>
    <meta charset="UTF-8" />
    <meta name="viewport" content="width=device-width, initial-scale=1.0" />
    <title>Tayyaba Sajjad — Biomedical × AI Engineering</title>
    <link rel="preconnect" href="https://fonts.googleapis.com" />
    <link rel="preconnect" href="https://fonts.gstatic.com" crossorigin />
    <link href="https://fonts.googleapis.com/css2?family=Space+Grotesk:wght@300;400;500;600;700&family=Inter:wght@300;400;500;600&display=swap" rel="stylesheet" />
    <link rel="stylesheet" href="https://cdnjs.cloudflare.com/ajax/libs/font-awesome/6.5.0/css/all.min.css" />
    <style>
        *, *::before, *::after {{ margin: 0; padding: 0; box-sizing: border-box; }}
        :root {{
            --bg: #0a0b1e;
            --bg-alt: #0d0f28;
            --card: rgba(255,255,255,0.05);
            --card-hover: rgba(255,255,255,0.08);
            --border: rgba(255,255,255,0.08);
            --border-hover: rgba(255,255,255,0.15);
            --gradient-1: linear-gradient(135deg, #6C63FF, #EC4899);
            --gradient-2: linear-gradient(135deg, #00D4AA, #06B6D4);
            --gradient-3: linear-gradient(135deg, #FF6B6B, #F59E0B);
            --gradient-4: linear-gradient(135deg, #A78BFA, #3B82F6);
            --gradient-hero: linear-gradient(135deg, #6C63FF 0%, #EC4899 50%, #FF6B6B 100%);
            --text: #f0f0f5;
            --text-secondary: rgba(255,255,255,0.6);
            --text-muted: rgba(255,255,255,0.35);
            --glow-purple: rgba(108,63,255,0.3);
            --glow-pink: rgba(236,72,153,0.3);
            --glow-teal: rgba(0,212,170,0.25);
            --font: 'Space Grotesk', -apple-system, BlinkMacSystemFont, sans-serif;
            --font-body: 'Inter', -apple-system, BlinkMacSystemFont, sans-serif;
        }}
        html {{ scroll-behavior: smooth; }}
        body {{
            background: var(--bg);
            color: var(--text);
            font-family: var(--font-body);
            line-height: 1.7;
            font-weight: 300;
            -webkit-font-smoothing: antialiased;
            overflow-x: hidden;
        }}
        a {{ color: inherit; text-decoration: none; }}
        img {{ max-width: 100%; display: block; }}

        ::-webkit-scrollbar {{ width: 6px; }}
        ::-webkit-scrollbar-track {{ background: var(--bg); }}
        ::-webkit-scrollbar-thumb {{ background: var(--gradient-1); border-radius: 3px; }}

        /* Gradient mesh background */
        .mesh-bg {{
            position: fixed; top: 0; left: 0; right: 0; bottom: 0;
            background:
                radial-gradient(ellipse 80% 50% at 50% -20%, rgba(108,63,255,0.12) 0%, transparent 60%),
                radial-gradient(ellipse 60% 50% at 80% 40%, rgba(236,72,153,0.08) 0%, transparent 50%),
                radial-gradient(ellipse 50% 40% at 20% 60%, rgba(0,212,170,0.06) 0%, transparent 50%);
            pointer-events: none; z-index: -1;
        }}

        /* === NAV === */
        nav {{
            position: fixed; top: 0; left: 0; right: 0; z-index: 100;
            padding: 20px 48px;
            display: flex; align-items: center; justify-content: space-between;
            transition: all 0.4s;
        }}
        nav.scrolled {{
            background: rgba(10,11,30,0.8);
            backdrop-filter: blur(24px);
            border-bottom: 1px solid var(--border);
        }}
        .nav-logo {{
            font-family: var(--font);
            font-size: 1.3rem; font-weight: 700;
            background: var(--gradient-1); -webkit-background-clip: text; -webkit-text-fill-color: transparent;
        }}
        .nav-links {{ display: flex; gap: 32px; list-style: none; align-items: center; }}
        .nav-links a {{
            font-size: 0.8rem; font-weight: 500; text-transform: uppercase; letter-spacing: 0.08em;
            color: var(--text-secondary); transition: color 0.3s; position: relative;
        }}
        .nav-links a::after {{
            content: '';
            position: absolute; bottom: -4px; left: 0; width: 0; height: 2px;
            background: var(--gradient-1); transition: width 0.3s; border-radius: 2px;
        }}
        .nav-links a:hover::after {{ width: 100%; }}
        .nav-links a:hover {{ color: var(--text); }}
        .nav-social a {{ font-size: 1rem; color: var(--text-muted); transition: color 0.3s; margin-left: 8px; }}
        .nav-social a:hover {{ color: #EC4899; }}

        /* === HERO === */
        .hero {{
            min-height: 100vh;
            display: grid;
            grid-template-columns: 1fr 1fr;
            align-items: center;
            padding: 0 48px;
            gap: 64px;
            position: relative;
            overflow: hidden;
        }}
        .hero::before {{
            content: '';
            position: absolute;
            top: -30%; right: -10%;
            width: 500px; height: 500px;
            background: radial-gradient(circle, rgba(108,63,255,0.15) 0%, transparent 70%);
            border-radius: 50%;
            pointer-events: none;
        }}
        .hero::after {{
            content: '';
            position: absolute;
            bottom: -20%; left: -5%;
            width: 400px; height: 400px;
            background: radial-gradient(circle, rgba(236,72,153,0.1) 0%, transparent 70%);
            border-radius: 50%;
            pointer-events: none;
        }}
        .hero-text {{ max-width: 580px; justify-self: end; }}
        .hero-label {{
            display: inline-block;
            font-size: 0.7rem; text-transform: uppercase; letter-spacing: 0.15em;
            font-weight: 600; color: #06B6D4;
            margin-bottom: 16px;
            padding: 6px 16px;
            border: 1px solid rgba(6,182,212,0.3);
            border-radius: 100px;
        }}
        .hero-name {{
            font-family: var(--font);
            font-size: clamp(3rem, 6vw, 5rem);
            font-weight: 700;
            line-height: 1.05;
            margin-bottom: 4px;
            background: var(--gradient-hero); -webkit-background-clip: text; -webkit-text-fill-color: transparent;
        }}
        .hero-title {{
            font-size: clamp(1rem, 1.8vw, 1.2rem);
            color: var(--text-secondary);
            font-weight: 400;
            margin-bottom: 24px;
        }}
        .hero-title strong {{ color: #00D4AA; font-weight: 600; }}
        .hero-bio {{
            color: var(--text-secondary);
            font-size: 0.95rem;
            line-height: 1.8;
            margin-bottom: 28px;
            max-width: 480px;
        }}
        .hero-bio strong {{ color: var(--text); font-weight: 600; }}
        .hero-stats {{
            display: flex; gap: 32px; margin-bottom: 32px; flex-wrap: wrap;
        }}
        .hero-stat-value {{
            font-family: var(--font);
            font-size: 2rem; font-weight: 700;
            background: var(--gradient-2); -webkit-background-clip: text; -webkit-text-fill-color: transparent;
        }}
        .hero-stat-label {{
            font-size: 0.7rem; text-transform: uppercase; letter-spacing: 0.08em;
            color: var(--text-muted); margin-top: 2px;
        }}
        .hero-actions {{
            display: flex; gap: 16px; flex-wrap: wrap;
        }}
        .btn {{
            padding: 14px 32px;
            font-family: var(--font);
            font-size: 0.85rem;
            font-weight: 600;
            text-transform: uppercase;
            letter-spacing: 0.06em;
            border: none;
            cursor: pointer;
            transition: all 0.3s;
            display: inline-flex;
            align-items: center;
            gap: 10px;
            border-radius: 8px;
        }}
        .btn-primary {{
            background: var(--gradient-1);
            color: #fff;
        }}
        .btn-primary:hover {{
            transform: translateY(-3px);
            box-shadow: 0 12px 32px var(--glow-purple);
        }}
        .btn-outline {{
            background: var(--card);
            color: var(--text);
            border: 1px solid var(--border);
            backdrop-filter: blur(12px);
        }}
        .btn-outline:hover {{
            border-color: #EC4899;
            color: #EC4899;
            transform: translateY(-3px);
        }}

        /* Hero Image */
        .hero-image {{ position: relative; justify-self: start; }}
        .hero-image-frame {{
            position: relative;
            width: 360px;
            height: 460px;
            border-radius: 20px;
            overflow: hidden;
            border: 1px solid var(--border);
        }}
        .hero-image-frame img {{
            width: 100%; height: 100%;
            object-fit: cover;
            transition: transform 0.6s;
        }}
        .hero-image-frame:hover img {{ transform: scale(1.03); }}
        .hero-image-glow {{
            position: absolute;
            top: -20px; left: -20px;
            width: calc(100% + 40px); height: calc(100% + 40px);
            background: var(--gradient-1);
            border-radius: 28px;
            z-index: -1;
            opacity: 0.2;
            filter: blur(24px);
        }}
        .hero-badge {{
            position: absolute;
            bottom: 24px; right: -20px;
            background: rgba(10,11,30,0.85);
            backdrop-filter: blur(16px);
            border: 1px solid var(--border);
            border-radius: 12px;
            padding: 14px 20px;
        }}
        .hero-badge span {{
            display: block;
            font-size: 0.65rem; text-transform: uppercase; letter-spacing: 0.1em;
            color: #06B6D4; font-weight: 600;
        }}
        .hero-badge strong {{
            font-family: var(--font);
            font-size: 1rem; font-weight: 600;
            background: var(--gradient-2); -webkit-background-clip: text; -webkit-text-fill-color: transparent;
        }}

        /* === SECTION COMMON === */
        section {{ padding: 100px 48px; position: relative; }}
        .section-inner {{ max-width: 1200px; margin: 0 auto; }}
        .section-header {{ margin-bottom: 56px; }}
        .section-number {{
            font-size: 0.7rem; text-transform: uppercase; letter-spacing: 0.2em;
            font-weight: 600; color: #06B6D4; margin-bottom: 8px;
        }}
        .section-heading {{
            font-family: var(--font);
            font-size: clamp(2rem, 3.5vw, 3rem);
            font-weight: 700;
            line-height: 1.15;
        }}
        .section-heading .gradient-text {{
            background: var(--gradient-1); -webkit-background-clip: text; -webkit-text-fill-color: transparent;
        }}
        .section-heading .gradient-text-2 {{
            background: var(--gradient-2); -webkit-background-clip: text; -webkit-text-fill-color: transparent;
        }}
        .section-heading .gradient-text-4 {{
            background: var(--gradient-4); -webkit-background-clip: text; -webkit-text-fill-color: transparent;
        }}
        .section-sub {{
            color: var(--text-secondary);
            font-size: 0.95rem;
            margin-top: 12px;
            line-height: 1.8;
            max-width: 560px;
        }}

        /* === ABOUT === */
        .about-grid {{
            display: grid;
            grid-template-columns: 1fr 1fr;
            gap: 64px;
            align-items: start;
        }}
        .about-text p {{
            color: var(--text-secondary);
            font-size: 0.95rem;
            line-height: 1.9;
            margin-bottom: 20px;
        }}
        .about-text p strong {{ color: var(--text); font-weight: 600; }}
        .about-text .highlight-text {{
            background: var(--gradient-2); -webkit-background-clip: text; -webkit-text-fill-color: transparent;
            font-weight: 600;
        }}
        .about-highlights {{
            display: grid;
            grid-template-columns: 1fr 1fr;
            gap: 16px;
        }}
        .about-highlight {{
            background: var(--card);
            border: 1px solid var(--border);
            border-radius: 16px;
            padding: 24px;
            backdrop-filter: blur(12px);
            transition: all 0.3s;
        }}
        .about-highlight:hover {{
            border-color: rgba(108,63,255,0.3);
            transform: translateY(-4px);
            box-shadow: 0 12px 32px rgba(108,63,255,0.1);
        }}
        .about-highlight-icon {{ font-size: 1.4rem; margin-bottom: 12px; }}
        .about-highlight-icon i {{ background: var(--gradient-1); -webkit-background-clip: text; -webkit-text-fill-color: transparent; }}
        .about-highlight h4 {{ font-size: 0.85rem; font-weight: 600; color: var(--text); margin-bottom: 6px; }}
        .about-highlight p {{ font-size: 0.8rem; color: var(--text-muted); line-height: 1.6; }}
        .cgpa-badge {{
            display: inline-block;
            background: var(--gradient-2);
            color: #fff;
            padding: 2px 10px;
            border-radius: 4px;
            font-size: 0.7rem;
            font-weight: 700;
            margin-left: 6px;
        }}

        /* === SKILLS === */
        .skills-grid {{
            display: grid;
            grid-template-columns: repeat(auto-fill, minmax(260px, 1fr));
            gap: 20px;
        }}
        .skill-card {{
            background: var(--card);
            border: 1px solid var(--border);
            border-radius: 16px;
            padding: 28px;
            backdrop-filter: blur(12px);
            transition: all 0.3s;
        }}
        .skill-card:hover {{
            border-color: rgba(236,72,153,0.3);
            transform: translateY(-4px);
            box-shadow: 0 12px 32px rgba(236,72,153,0.1);
        }}
        .skill-card-icon {{ font-size: 1.5rem; margin-bottom: 16px; }}
        .skill-card-icon i {{ background: var(--gradient-3); -webkit-background-clip: text; -webkit-text-fill-color: transparent; }}
        .skill-card h3 {{ font-size: 0.95rem; font-weight: 600; color: var(--text); margin-bottom: 8px; }}
        .skill-card p {{ font-size: 0.82rem; color: var(--text-secondary); line-height: 1.7; }}
        .skill-tags {{ display: flex; flex-wrap: wrap; gap: 6px; margin-top: 12px; }}
        .skill-tag {{
            font-size: 0.65rem; text-transform: uppercase; letter-spacing: 0.06em;
            padding: 4px 10px; border-radius: 4px;
            background: rgba(255,255,255,0.04);
            color: var(--text-muted);
        }}

        /* === TIMELINE / EXPERIENCE === */
        .timeline {{ position: relative; padding-left: 32px; }}
        .timeline::before {{
            content: '';
            position: absolute; left: 11px; top: 8px; bottom: 8px;
            width: 2px;
            background: linear-gradient(180deg, #6C63FF, #EC4899, #00D4AA, #A78BFA);
            border-radius: 2px;
        }}
        .timeline-item {{ position: relative; margin-bottom: 48px; }}
        .timeline-item:last-child {{ margin-bottom: 0; }}
        .timeline-dot {{
            position: absolute; left: -27px; top: 6px;
            width: 14px; height: 14px; border-radius: 50%;
            background: var(--bg);
            border: 3px solid #6C63FF;
        }}
        .timeline-item:nth-child(1) .timeline-dot {{ border-color: #6C63FF; }}
        .timeline-item:nth-child(2) .timeline-dot {{ border-color: #EC4899; }}
        .timeline-item:nth-child(3) .timeline-dot {{ border-color: #00D4AA; }}
        .timeline-item:nth-child(4) .timeline-dot {{ border-color: #F59E0B; }}
        .timeline-item:nth-child(5) .timeline-dot {{ border-color: #A78BFA; }}
        .timeline-item:nth-child(6) .timeline-dot {{ border-color: #3B82F6; }}
        .timeline-date {{
            font-size: 0.7rem; text-transform: uppercase; letter-spacing: 0.1em;
            font-weight: 600; color: #06B6D4; margin-bottom: 4px;
        }}
        .timeline-role {{
            font-family: var(--font);
            font-size: 1.2rem; font-weight: 600; color: var(--text); margin-bottom: 2px;
        }}
        .timeline-company {{
            font-size: 0.85rem; color: var(--text-muted); margin-bottom: 10px;
        }}
        .timeline-desc {{
            font-size: 0.88rem; color: var(--text-secondary); line-height: 1.8;
        }}
        .timeline-tags {{ display: flex; flex-wrap: wrap; gap: 6px; margin-top: 10px; }}
        .timeline-tag {{
            font-size: 0.65rem; padding: 3px 10px; border-radius: 4px;
            background: rgba(108,63,255,0.08);
            color: rgba(108,63,255,0.7);
            border: 1px solid rgba(108,63,255,0.15);
        }}

        /* === PROJECTS === */
        .projects-grid {{
            display: grid;
            grid-template-columns: repeat(auto-fill, minmax(340px, 1fr));
            gap: 24px;
        }}
        .project-card {{
            background: var(--card);
            border: 1px solid var(--border);
            border-radius: 16px;
            padding: 32px;
            backdrop-filter: blur(12px);
            transition: all 0.4s;
            display: flex; flex-direction: column;
        }}
        .project-card:hover {{
            border-color: rgba(0,212,170,0.3);
            transform: translateY(-6px);
            box-shadow: 0 20px 48px rgba(0,0,0,0.2), 0 0 40px rgba(0,212,170,0.05);
        }}
        .project-icon {{ font-size: 1.8rem; margin-bottom: 16px; }}
        .project-icon i {{ background: var(--gradient-2); -webkit-background-clip: text; -webkit-text-fill-color: transparent; }}
        .project-card h3 {{
            font-family: var(--font);
            font-size: 1.05rem; font-weight: 600; color: var(--text);
            margin-bottom: 8px;
        }}
        .project-card p {{
            font-size: 0.85rem; color: var(--text-secondary);
            line-height: 1.7; margin-bottom: 16px; flex: 1;
        }}
        .project-tech {{ display: flex; flex-wrap: wrap; gap: 6px; margin-bottom: 16px; }}
        .project-tech span {{
            font-size: 0.65rem; padding: 4px 10px; border-radius: 4px;
            background: rgba(255,255,255,0.05);
            color: var(--text-muted);
        }}
        .project-links {{ display: flex; gap: 16px; }}
        .project-links a {{
            font-size: 0.75rem; text-transform: uppercase; letter-spacing: 0.06em;
            font-weight: 600;
            color: var(--text-muted); transition: color 0.3s;
            display: inline-flex; align-items: center; gap: 6px;
        }}
        .project-links a:hover {{ color: #00D4AA; }}

        /* === PUBLICATIONS === */
        .pub-card {{
            background: var(--card);
            border: 1px solid var(--border);
            border-radius: 16px;
            padding: 28px 32px;
            margin-bottom: 16px;
            transition: all 0.3s;
        }}
        .pub-card:hover {{ border-color: rgba(108,63,255,0.3); }}
        .pub-title {{
            font-family: var(--font);
            font-size: 1rem; font-weight: 600; color: var(--text);
            margin-bottom: 6px; line-height: 1.4;
        }}
        .pub-venue {{
            font-size: 0.8rem; color: #00D4AA; font-weight: 500; margin-bottom: 4px;
        }}
        .pub-status {{
            font-size: 0.65rem; text-transform: uppercase; letter-spacing: 0.08em;
            padding: 3px 12px; border-radius: 100px; display: inline-block;
            font-weight: 600;
        }}
        .pub-status.under-review {{
            background: rgba(245,158,11,0.12);
            color: #F59E0B;
            border: 1px solid rgba(245,158,11,0.2);
        }}
        .pub-status.published {{
            background: rgba(0,212,170,0.12);
            color: #00D4AA;
            border: 1px solid rgba(0,212,170,0.2);
        }}

        /* === LEADERSHIP === */
        .lead-grid {{
            display: grid;
            grid-template-columns: repeat(auto-fill, minmax(300px, 1fr));
            gap: 20px;
        }}
        .lead-card {{
            background: var(--card);
            border: 1px solid var(--border);
            border-radius: 16px;
            padding: 28px;
            backdrop-filter: blur(12px);
            transition: all 0.3s;
        }}
        .lead-card:hover {{
            border-color: rgba(236,72,153,0.3);
            transform: translateY(-4px);
            box-shadow: 0 12px 32px rgba(236,72,153,0.1);
        }}
        .lead-icon {{ font-size: 1.5rem; margin-bottom: 14px; }}
        .lead-icon i {{ background: var(--gradient-3); -webkit-background-clip: text; -webkit-text-fill-color: transparent; }}
        .lead-card h3 {{ font-size: 0.95rem; font-weight: 600; color: var(--text); margin-bottom: 2px; }}
        .lead-org-date {{ font-size: 0.78rem; color: var(--text-muted); margin-bottom: 10px; }}
        .lead-card p {{ font-size: 0.82rem; color: var(--text-secondary); line-height: 1.7; }}

        /* === AWARDS === */
        .awards-grid {{
            display: grid;
            grid-template-columns: repeat(auto-fill, minmax(300px, 1fr));
            gap: 16px;
        }}
        .award-card {{
            background: var(--card);
            border: 1px solid var(--border);
            border-radius: 16px;
            padding: 24px;
            display: flex; align-items: flex-start; gap: 16px;
            transition: all 0.3s;
        }}
        .award-card:hover {{ border-color: rgba(245,158,11,0.3); }}
        .award-icon {{ font-size: 1.3rem; margin-top: 2px; }}
        .award-icon i {{ background: var(--gradient-3); -webkit-background-clip: text; -webkit-text-fill-color: transparent; }}
        .award-card h4 {{ font-size: 0.85rem; font-weight: 600; color: var(--text); margin-bottom: 2px; }}
        .award-card p {{ font-size: 0.78rem; color: var(--text-muted); }}

        /* === CONTACT === */
        .contact-grid {{
            display: grid;
            grid-template-columns: 1fr 1fr;
            gap: 64px;
        }}
        .contact-info p {{
            color: var(--text-secondary); font-size: 0.95rem; line-height: 1.8;
            margin-bottom: 32px;
        }}
        .contact-detail {{
            display: flex; align-items: center; gap: 14px;
            margin-bottom: 16px;
        }}
        .contact-detail i {{ width: 20px; font-size: 1rem; }}
        .contact-detail i.fa-envelope {{ color: #EC4899; }}
        .contact-detail i.fa-github {{ color: #6C63FF; }}
        .contact-detail i.fa-linkedin-in {{ color: #00D4AA; }}
        .contact-detail i.fa-map-marker-alt {{ color: #F59E0B; }}
        .contact-detail i.fa-phone {{ color: #A78BFA; }}
        .contact-detail span, .contact-detail a {{
            font-size: 0.9rem; color: var(--text-secondary);
        }}
        .contact-detail a {{ transition: color 0.3s; }}
        .contact-detail a:hover {{ color: var(--text); }}
        .contact-form {{ display: flex; flex-direction: column; gap: 16px; }}
        .contact-form input,
        .contact-form textarea {{
            background: var(--card);
            border: 1px solid var(--border);
            border-radius: 12px;
            padding: 16px 18px;
            font-family: var(--font-body);
            font-size: 0.85rem;
            color: var(--text);
            outline: none;
            transition: border-color 0.3s;
        }}
        .contact-form input:focus,
        .contact-form textarea:focus {{ border-color: #6C63FF; }}
        .contact-form textarea {{ min-height: 140px; resize: vertical; }}
        .contact-form button {{ align-self: flex-start; }}
        .form-success {{
            display: none;
            background: rgba(0,212,170,0.1);
            border: 1px solid rgba(0,212,170,0.3);
            border-radius: 12px;
            padding: 20px;
            color: #00D4AA;
            font-size: 0.9rem;
            text-align: center;
        }}
        .form-success.show {{ display: block; }}

        /* === FOOTER === */
        footer {{
            border-top: 1px solid var(--border);
            padding: 40px 48px;
            display: flex;
            justify-content: space-between;
            align-items: center;
        }}
        footer p {{ font-size: 0.8rem; color: var(--text-muted); }}
        footer .social-links {{ display: flex; gap: 20px; }}
        footer .social-links a {{
            font-size: 1.1rem; color: var(--text-muted);
            transition: color 0.3s;
        }}
        footer .social-links a:hover {{ color: #EC4899; }}

        /* === ANIMATIONS === */
        .fade-in {{
            opacity: 0; transform: translateY(24px);
            transition: opacity 0.6s ease, transform 0.6s ease;
        }}
        .fade-in.visible {{
            opacity: 1; transform: translateY(0);
        }}
        .fade-in-delay-1 {{ transition-delay: 0.1s; }}
        .fade-in-delay-2 {{ transition-delay: 0.2s; }}
        .fade-in-delay-3 {{ transition-delay: 0.3s; }}
        .fade-in-delay-4 {{ transition-delay: 0.4s; }}
        .fade-in-delay-5 {{ transition-delay: 0.5s; }}

        /* === RESPONSIVE === */
        @media (max-width: 1024px) {{
            .hero {{ grid-template-columns: 1fr; padding: 120px 32px 60px; gap: 48px; }}
            .hero-text {{ justify-self: center; text-align: center; }}
            .hero-bio {{ margin: 0 auto 28px; }}
            .hero-stats {{ justify-content: center; }}
            .hero-actions {{ justify-content: center; }}
            .hero-image {{ justify-self: center; }}
            .hero-badge {{ right: 0; }}
            .about-grid {{ grid-template-columns: 1fr; gap: 40px; }}
            .contact-grid {{ grid-template-columns: 1fr; gap: 40px; }}
            nav {{ padding: 16px 24px; }}
            section {{ padding: 80px 24px; }}
            footer {{ padding: 32px 24px; flex-direction: column; gap: 16px; text-align: center; }}
        }}
        @media (max-width: 640px) {{
            .nav-links {{ display: none; }}
            .hero {{ padding: 100px 20px 40px; }}
            .hero-image-frame {{ width: 260px; height: 340px; }}
            .hero-stats {{ gap: 20px; flex-wrap: wrap; }}
            .about-highlights {{ grid-template-columns: 1fr; }}
            .projects-grid {{ grid-template-columns: 1fr; }}
            .skills-grid {{ grid-template-columns: 1fr; }}
            .lead-grid {{ grid-template-columns: 1fr; }}
            .awards-grid {{ grid-template-columns: 1fr; }}
            section {{ padding: 60px 20px; }}
        }}
    </style>
</head>
<body>

    <div class="mesh-bg"></div>

    <!-- ====== NAV ====== -->
    <nav id="navbar">
        <div class="nav-logo">Tayyaba.</div>
        <ul class="nav-links">
            <li><a href="#about">About</a></li>
            <li><a href="#skills">Skills</a></li>
            <li><a href="#experience">Experience</a></li>
            <li><a href="#projects">Projects</a></li>
            <li><a href="#publications">Research</a></li>
            <li><a href="#leadership">Leadership</a></li>
            <li><a href="#contact">Contact</a></li>
            <li class="nav-social">
                <a href="https://github.com/tayyaba-code" target="_blank" rel="noopener" aria-label="GitHub"><i class="fab fa-github"></i></a>
                <a href="https://linkedin.com/in/tayyabasajjad" target="_blank" rel="noopener" aria-label="LinkedIn"><i class="fab fa-linkedin-in"></i></a>
            </li>
        </ul>
    </nav>

    <!-- ====== HERO ====== -->
    <section class="hero" id="hero">
        <div class="hero-text">
            <div class="hero-label">Biomedical × AI Engineering</div>
            <h1 class="hero-name">Tayyaba<br />Sajjad</h1>
            <div class="hero-title">ML/AI Engineer &amp; <strong>Biomedical Engineer</strong></div>
            <p class="hero-bio">
                Final-year <strong>BS Biomedical Engineering</strong> student at <strong>UET Lahore</strong> 
                (<span style="color:#00D4AA;font-weight:600;">CGPA 3.76/4.0</span>) with <strong>3+ years</strong> 
                of hands-on ML/AI engineering experience spanning <strong>medical imaging, real-time computer vision, 
                clinical prediction, and NLP</strong>. Author of 3 peer-reviewed publications and sole/lead developer 
                of <strong>10+ end-to-end ML/DL systems</strong> — from raw data to deployed APIs.
            </p>
            <div class="hero-stats">
                <div>
                    <div class="hero-stat-value">3.76</div>
                    <div class="hero-stat-label">CGPA</div>
                </div>
                <div>
                    <div class="hero-stat-value">10+</div>
                    <div class="hero-stat-label">AI Projects</div>
                </div>
                <div>
                    <div class="hero-stat-value">8</div>
                    <div class="hero-stat-label">GitHub Repos</div>
                </div>
                <div>
                    <div class="hero-stat-value">3</div>
                    <div class="hero-stat-label">Publications</div>
                </div>
            </div>
            <div class="hero-actions">
                <a href="#projects" class="btn btn-primary">View Projects <i class="fas fa-arrow-right"></i></a>
                <a href="https://github.com/tayyaba-code" target="_blank" rel="noopener" class="btn btn-outline"><i class="fab fa-github"></i> GitHub</a>
                <a href="#contact" class="btn btn-outline">Get in Touch</a>
            </div>
        </div>
        <div class="hero-image">
            <div class="hero-image-frame">
                <img src="data:image/jpeg;base64,{img_b64}" alt="Tayyaba Sajjad" />
                <div class="hero-image-glow"></div>
            </div>
            <div class="hero-badge">
                <span>Currently</span>
                <strong>AI Engineer Intern</strong>
            </div>
        </div>
    </section>

    <!-- ====== ABOUT ====== -->
    <section id="about">
        <div class="section-inner">
            <div class="section-header">
                <div class="section-number">01 — About</div>
                <h2 class="section-heading">Bridging <span class="gradient-text">biology</span> and <span class="gradient-text-2">code</span></h2>
                <p class="section-sub">
                    I engineer AI systems for clinical impact and build production-grade software pipelines — 
                    because healthcare shouldn't have to choose between a medical expert and a software engineer.
                </p>
            </div>
            <div class="about-grid">
                <div class="about-text">
                    <p>
                        I'm a <strong>final-year BS Biomedical Engineering</strong> student at <strong>UET Lahore</strong> 
                        with a <strong>CGPA of 3.76/4.0</strong><span class="cgpa-badge">Top Tier</span> — 
                        but my real education happened at the intersection of <strong>Machine Learning, Deep Learning, 
                        Computer Vision, and NLP</strong>. I've built everything from medical image classifiers to 
                        production-ready FastAPI pipelines, from real-time emotion detection to drug discovery models.
                    </p>
                    <p>
                        Currently serving as <strong>AI Engineer Intern at CodeCliex</strong>, 
                        <strong>AI &amp; ML Engineer Intern at Inquisitor Society</strong>, and 
                        <strong>Managing Director at IEEE UET Lahore</strong>. Previously interned as a 
                        <strong>Biomedical Engineer at Mediequips</strong> and served as 
                        <strong>Girls Coordinator at Blood Donor Society</strong> and 
                        <strong>Technical Director at IET, UET</strong>.
                    </p>
                    <p>
                        <strong>Tech stack:</strong> Python, TensorFlow, PyTorch, Scikit-learn, XGBoost, LightGBM, 
                        OpenCV, MediaPipe, DeepFace, YOLO, LangChain, LangGraph, Ollama, FastAPI, Flask, Docker, 
                        Git, PostgreSQL, and MATLAB. I don't just know the tools — I know when and why to use them.
                    </p>
                </div>
                <div class="about-highlights">
                    <div class="about-highlight">
                        <div class="about-highlight-icon"><i class="fas fa-graduation-cap"></i></div>
                        <h4>Biomedical Engineering</h4>
                        <p>UET Lahore · CGPA 3.76/4.0 · Final Year</p>
                    </div>
                    <div class="about-highlight">
                        <div class="about-highlight-icon"><i class="fas fa-robot"></i></div>
                        <h4>ML / AI Engineering</h4>
                        <p>3+ years · 10+ systems · Medical AI specialist</p>
                    </div>
                    <div class="about-highlight">
                        <div class="about-highlight-icon"><i class="fas fa-flask"></i></div>
                        <h4>Research</h4>
                        <p>3 publications under review · Springer 2026</p>
                    </div>
                    <div class="about-highlight">
                        <div class="about-highlight-icon"><i class="fas fa-users"></i></div>
                        <h4>Leadership</h4>
                        <p>Managing Director @ IEEE · Girls Coordinator @ BDS · Tech Director @ IET</p>
                    </div>
                </div>
            </div>
        </div>
    </section>

    <!-- ====== SKILLS ====== -->
    <section id="skills" style="background:var(--bg-alt);">
        <div class="section-inner">
            <div class="section-header">
                <div class="section-number">02 — Skills</div>
                <h2 class="section-heading">Full-stack <span class="gradient-text">AI Engineering</span></h2>
                <p class="section-sub">From medical imaging pipelines to LLM-powered applications — I build across the entire AI stack.</p>
            </div>
            <div class="skills-grid">
                <div class="skill-card">
                    <div class="skill-card-icon"><i class="fas fa-brain"></i></div>
                    <h3>Machine &amp; Deep Learning</h3>
                    <p>CNN, ANN, LSTM, Transformers, ESRGAN/RRDBNet, YOLO — building and optimizing models for clinical and real-world applications.</p>
                    <div class="skill-tags">
                        <span class="skill-tag">TensorFlow</span>
                        <span class="skill-tag">Keras</span>
                        <span class="skill-tag">Scikit-learn</span>
                        <span class="skill-tag">XGBoost</span>
                        <span class="skill-tag">LightGBM</span>
                    </div>
                </div>
                <div class="skill-card">
                    <div class="skill-card-icon"><i class="fas fa-eye"></i></div>
                    <h3>Computer Vision</h3>
                    <p>Medical imaging, real-time video pipelines, pose estimation, facial recognition, and super-resolution for clinical diagnostics.</p>
                    <div class="skill-tags">
                        <span class="skill-tag">OpenCV</span>
                        <span class="skill-tag">MediaPipe</span>
                        <span class="skill-tag">DeepFace</span>
                        <span class="skill-tag">YOLO</span>
                        <span class="skill-tag">ESRGAN</span>
                    </div>
                </div>
                <div class="skill-card">
                    <div class="skill-card-icon"><i class="fas fa-language"></i></div>
                    <h3>Generative AI &amp; LLMs</h3>
                    <p>Building LLM-powered applications with LangChain, LangGraph, and Ollama. RAG pipelines, agentic workflows, and prompt engineering.</p>
                    <div class="skill-tags">
                        <span class="skill-tag">LangChain</span>
                        <span class="skill-tag">LangGraph</span>
                        <span class="skill-tag">Ollama</span>
                        <span class="skill-tag">Generative AI</span>
                    </div>
                </div>
                <div class="skill-card">
                    <div class="skill-card-icon"><i class="fas fa-code-branch"></i></div>
                    <h3>MLOps &amp; Deployment</h3>
                    <p>End-to-end ML pipeline deployment — from data ingestion to production APIs with monitoring and version control.</p>
                    <div class="skill-tags">
                        <span class="skill-tag">FastAPI</span>
                        <span class="skill-tag">Flask</span>
                        <span class="skill-tag">Docker</span>
                        <span class="skill-tag">REST API</span>
                        <span class="skill-tag">Git/GitHub</span>
                    </div>
                </div>
                <div class="skill-card">
                    <div class="skill-card-icon"><i class="fas fa-dna"></i></div>
                    <h3>NLP &amp; Bioinformatics</h3>
                    <p>QSAR modelling, molecular property prediction, text classification, clinical NLP for extracting insights from unstructured healthcare data.</p>
                    <div class="skill-tags">
                        <span class="skill-tag">Transformers</span>
                        <span class="skill-tag">BERT</span>
                        <span class="skill-tag">NLTK</span>
                        <span class="skill-tag">RDKit</span>
                    </div>
                </div>
                <div class="skill-card">
                    <div class="skill-card-icon"><i class="fas fa-table"></i></div>
                    <h3>Data Engineering &amp; Analytics</h3>
                    <p>Feature engineering, SMOTE, PCA, SHAP explainability, statistical analysis, and data visualization for model interpretability.</p>
                    <div class="skill-tags">
                        <span class="skill-tag">NumPy</span>
                        <span class="skill-tag">Pandas</span>
                        <span class="skill-tag">Matplotlib</span>
                        <span class="skill-tag">Seaborn</span>
                        <span class="skill-tag">SHAP</span>
                    </div>
                </div>
            </div>
        </div>
    </section>

    <!-- ====== EXPERIENCE ====== -->
    <section id="experience">
        <div class="section-inner">
            <div class="section-header">
                <div class="section-number">03 — Experience</div>
                <h2 class="section-heading">Where I've <span class="gradient-text">grown</span></h2>
                <p class="section-sub">From AI engineering to biomedical internships to IEEE leadership — every step deepened my conviction that healthcare + AI is the future.</p>
            </div>
            <div class="timeline">
                <div class="timeline-item fade-in">
                    <div class="timeline-dot"></div>
                    <div class="timeline-date">Present</div>
                    <div class="timeline-role">AI Engineer Intern</div>
                    <div class="timeline-company">CodeCliex</div>
                    <div class="timeline-desc">
                        Building and deploying production-grade AI models for clinical applications. Working on end-to-end ML pipelines including data ingestion, model training, optimization, and deployment via FastAPI/Flask APIs. Integrating LLM-based solutions using LangChain and LangGraph for healthcare automation.
                    </div>
                    <div class="timeline-tags">
                        <span class="timeline-tag">ML Pipelines</span>
                        <span class="timeline-tag">FastAPI</span>
                        <span class="timeline-tag">LangChain</span>
                        <span class="timeline-tag">Docker</span>
                    </div>
                </div>

                <div class="timeline-item fade-in fade-in-delay-1">
                    <div class="timeline-dot"></div>
                    <div class="timeline-date">Present</div>
                    <div class="timeline-role">AI &amp; ML Engineer Intern</div>
                    <div class="timeline-company">Inquisitor Society</div>
                    <div class="timeline-desc">
                        Developing ML models for real-world data analysis with focus on computer vision and NLP projects. Hands-on experience in data preprocessing, feature engineering, model training, evaluation, and deployment. Contributing to research-oriented AI solutions.
                    </div>
                    <div class="timeline-tags">
                        <span class="timeline-tag">Data Science</span>
                        <span class="timeline-tag">Computer Vision</span>
                        <span class="timeline-tag">NLP</span>
                        <span class="timeline-tag">MLOps</span>
                    </div>
                </div>

                <div class="timeline-item fade-in fade-in-delay-2">
                    <div class="timeline-dot"></div>
                    <div class="timeline-date">2025</div>
                    <div class="timeline-role">Biomedical Engineer Intern</div>
                    <div class="timeline-company">Mediequips</div>
                    <div class="timeline-desc">
                        Worked on biomedical equipment and systems integration. Applied engineering principles to healthcare technology, gaining practical experience in medical instrumentation and device management.
                    </div>
                    <div class="timeline-tags">
                        <span class="timeline-tag">Medical Instrumentation</span>
                        <span class="timeline-tag">Biosignal Processing</span>
                        <span class="timeline-tag">Healthcare Tech</span>
                    </div>
                </div>

                <div class="timeline-item fade-in fade-in-delay-3">
                    <div class="timeline-dot"></div>
                    <div class="timeline-date">Jan 2026 — Present</div>
                    <div class="timeline-role">Managing Director</div>
                    <div class="timeline-company">IEEE Society · UET Lahore</div>
                    <div class="timeline-desc">
                        Directing research initiatives across student chapters, sourcing industry speakers, and growing outreach event attendance by 40%. Coordinating student-industry networking sessions, connecting 100+ engineering students with AI/tech practitioners.
                    </div>
                    <div class="timeline-tags">
                        <span class="timeline-tag">Leadership</span>
                        <span class="timeline-tag">Research</span>
                        <span class="timeline-tag">Outreach</span>
                        <span class="timeline-tag">Events</span>
                    </div>
                </div>

                <div class="timeline-item fade-in fade-in-delay-4">
                    <div class="timeline-dot"></div>
                    <div class="timeline-date">Sep 2025 — May 2026</div>
                    <div class="timeline-role">Technical Director</div>
                    <div class="timeline-company">Institute of Engineering &amp; Technology · UET</div>
                    <div class="timeline-desc">
                        Managed end-to-end technical delivery for six student engineering events. Led a 12-person cross-functional team with zero missed deadlines. Mentored junior members in project scoping, iterative development, and stakeholder communication.
                    </div>
                    <div class="timeline-tags">
                        <span class="timeline-tag">Team Leadership</span>
                        <span class="timeline-tag">Project Management</span>
                        <span class="timeline-tag">Mentorship</span>
                    </div>
                </div>

                <div class="timeline-item fade-in fade-in-delay-5">
                    <div class="timeline-dot"></div>
                    <div class="timeline-date">Sep 2025 — May 2026</div>
                    <div class="timeline-role">Girls Coordinator</div>
                    <div class="timeline-company">Blood Donor Society · UET Lahore</div>
                    <div class="timeline-desc">
                        Increased registered female volunteer count by 30% across two semesters through targeted outreach and structured onboarding. Organized blood donation drives and awareness campaigns on campus.
                    </div>
                    <div class="timeline-tags">
                        <span class="timeline-tag">Outreach</span>
                        <span class="timeline-tag">Team Management</span>
                        <span class="timeline-tag">Healthcare</span>
                    </div>
                </div>
            </div>
        </div>
    </section>

    <!-- ====== PROJECTS ====== -->
    <section id="projects" style="background:var(--bg-alt);">
        <div class="section-inner">
            <div class="section-header">
                <div class="section-number">04 — Projects</div>
                <h2 class="section-heading">What I've <span class="gradient-text-2">built</span></h2>
                <p class="section-sub">Each project represents a problem I was curious about — and a solution I couldn't stop until it worked.</p>
            </div>
            <div class="projects-grid">
                <div class="project-card fade-in">
                    <div class="project-icon"><i class="fas fa-eye"></i></div>
                    <h3>Retinal Detachment Severity Classification</h3>
                    <p>Multi-class CNN to automatically grade retinal detachment severity from fundus images. Built custom augmentation and class-rebalancing pipeline for severe label imbalance across four severity grades. Validated against ophthalmologist annotations.</p>
                    <div class="project-tech">
                        <span>TensorFlow</span><span>OpenCV</span><span>Medical Imaging</span><span>CNN</span>
                    </div>
                    <div class="project-links">
                        <a href="https://github.com/tayyaba-code/Deep-Learning" target="_blank" rel="noopener"><i class="fab fa-github"></i> View Code</a>
                    </div>
                </div>

                <div class="project-card fade-in fade-in-delay-1">
                    <div class="project-icon"><i class="fas fa-brain"></i></div>
                    <h3>Neuro-Covid DWI Scan Enhancement — ESRGAN</h3>
                    <p>Adapted RRDBNet architecture for single-plane MRI super-resolution, improving perceptual quality of low-resolution DWI scans degraded by Covid-19 acquisition constraints. Evaluated using PSNR/SSIM metrics with radiologist confirmation.</p>
                    <div class="project-tech">
                        <span>Deep Learning</span><span>ESRGAN</span><span>RRDBNet</span><span>Medical Imaging</span>
                    </div>
                    <div class="project-links">
                        <a href="https://github.com/tayyaba-code/Deep-Learning" target="_blank" rel="noopener"><i class="fab fa-github"></i> View Code</a>
                    </div>
                </div>

                <div class="project-card fade-in fade-in-delay-2">
                    <div class="project-icon"><i class="fas fa-smile"></i></div>
                    <h3>Real-Time Human Emotion Detection</h3>
                    <p>Live-stream emotion classifier combining DeepFace 7-class facial expression recognition with MediaPipe face-mesh for robust landmark alignment. Optimised inference to under 60ms per frame on CPU with modular pipeline.</p>
                    <div class="project-tech">
                        <span>DeepFace</span><span>MediaPipe</span><span>OpenCV</span><span>Python</span>
                    </div>
                    <div class="project-links">
                        <a href="https://github.com/tayyaba-code/Machine-Learning" target="_blank" rel="noopener"><i class="fab fa-github"></i> View Code</a>
                    </div>
                </div>

                <div class="project-card fade-in fade-in-delay-3">
                    <div class="project-icon"><i class="fas fa-bone"></i></div>
                    <h3>Human Posture Correction via Landmark Analysis</h3>
                    <p>Real-time bad-posture detector using 33-point MediaPipe skeletal landmarks and eye-gaze angle estimation. Integrated audio and on-screen alerts with correction latency under 120ms for desk-worker ergonomics.</p>
                    <div class="project-tech">
                        <span>MediaPipe</span><span>OpenCV</span><span>Pose Estimation</span><span>Python</span>
                    </div>
                    <div class="project-links">
                        <a href="https://github.com/tayyaba-code/Machine-Learning" target="_blank" rel="noopener"><i class="fab fa-github"></i> View Code</a>
                    </div>
                </div>

                <div class="project-card fade-in fade-in-delay-4">
                    <div class="project-icon"><i class="fas fa-microchip"></i></div>
                    <h3>VocalID — Voice-Based Identification</h3>
                    <p>Voice recognition and speaker identification system using deep learning. Extracts MFCC features and uses neural networks for biometric voice authentication with high accuracy across multiple speakers.</p>
                    <div class="project-tech">
                        <span>TensorFlow</span><span>Librosa</span><span>Audio Processing</span><span>Python</span>
                    </div>
                    <div class="project-links">
                        <a href="https://github.com/tayyaba-code/VocalID" target="_blank" rel="noopener"><i class="fab fa-github"></i> View Code</a>
                    </div>
                </div>

                <div class="project-card fade-in fade-in-delay-4">
                    <div class="project-icon"><i class="fas fa-heartbeat"></i></div>
                    <h3>Anemia Detection from Complete Blood Count</h3>
                    <p>Trained and benchmarked six ML classifiers (RF, SVM, XGBoost, KNN, Logistic Regression, MLP) on CBC datasets. Applied SMOTE oversampling and SHAP explainability, achieving F1-score above 0.94.</p>
                    <div class="project-tech">
                        <span>Scikit-learn</span><span>SMOTE</span><span>SHAP</span><span>Feature Engineering</span>
                    </div>
                    <div class="project-links">
                        <a href="https://github.com/tayyaba-code/Machine-Learning" target="_blank" rel="noopener"><i class="fab fa-github"></i> View Code</a>
                    </div>
                </div>

                <div class="project-card fade-in fade-in-delay-3">
                    <div class="project-icon"><i class="fas fa-activity"></i></div>
                    <h3>Diabetes Risk Prediction — Flask API</h3>
                    <p>Engineered 12 domain-informed features from clinical records. Deployed XGBoost model as a Flask REST API with stratified 10-fold cross-validation for real-time patient risk scoring.</p>
                    <div class="project-tech">
                        <span>XGBoost</span><span>Flask</span><span>REST API</span><span>Python</span>
                    </div>
                    <div class="project-links">
                        <a href="https://github.com/tayyaba-code/Machine-Learning" target="_blank" rel="noopener"><i class="fab fa-github"></i> View Code</a>
                    </div>
                </div>

                <div class="project-card fade-in fade-in-delay-2">
                    <div class="project-icon"><i class="fas fa-ribbon"></i></div>
                    <h3>Breast Cancer Detection — ML Pipeline</h3>
                    <p>Processed Wisconsin Breast Cancer dataset end-to-end with outlier removal, correlation-based feature pruning, and normalization. Compared five classifiers achieving 98.2% accuracy with tuned SVM.</p>
                    <div class="project-tech">
                        <span>Scikit-learn</span><span>SVM</span><span>EDA</span><span>Python</span>
                    </div>
                    <div class="project-links">
                        <a href="https://github.com/tayyaba-code/Machine-Learning" target="_blank" rel="noopener"><i class="fab fa-github"></i> View Code</a>
                    </div>
                </div>

                <div class="project-card fade-in fade-in-delay-1">
                    <div class="project-icon"><i class="fas fa-walking"></i></div>
                    <h3>AI Gait Analysis System</h3>
                    <p>Video-based gait analysis pipeline extracting cadence, stride length, and joint-angle symmetry metrics from walk-cycle video. Applicable to post-surgical rehabilitation monitoring using MediaPipe.</p>
                    <div class="project-tech">
                        <span>MediaPipe</span><span>Biomechanics</span><span>Python</span><span>Computer Vision</span>
                    </div>
                    <div class="project-links">
                        <a href="https://github.com/tayyaba-code/Machine-Learning" target="_blank" rel="noopener"><i class="fab fa-github"></i> View Code</a>
                    </div>
                </div>

                <div class="project-card fade-in">
                    <div class="project-icon"><i class="fas fa-dna"></i></div>
                    <h3>Cancer Prognosis from Multi-Gene Expression</h3>
                    <p>Integrated multi-gene RNA-seq expression profiles into an ensemble model (RF + XGBoost) for personalized cancer prognosis. Applied PCA for dimensionality reduction and SHAP for gene signature explainability.</p>
                    <div class="project-tech">
                        <span>Bioinformatics</span><span>Ensemble ML</span><span>SHAP</span><span>RNA-seq</span>
                    </div>
                    <div class="project-links">
                        <a href="https://github.com/tayyaba-code/ml-dl-nlp-basics" target="_blank" rel="noopener"><i class="fab fa-github"></i> View Code</a>
                    </div>
                </div>

                <div class="project-card fade-in fade-in-delay-1">
                    <div class="project-icon"><i class="fas fa-flask"></i></div>
                    <h3>QSAR Modelling for Drug Discovery</h3>
                    <p>Quantitative Structure-Activity Relationship models to predict molecular properties using cheminformatics. Applied ML algorithms including Random Forest and XGBoost to accelerate virtual drug screening pipelines.</p>
                    <div class="project-tech">
                        <span>RDKit</span><span>Scikit-learn</span><span>Python</span><span>Cheminformatics</span>
                    </div>
                    <div class="project-links">
                        <a href="https://github.com/tayyaba-code/ml-dl-nlp-basics" target="_blank" rel="noopener"><i class="fab fa-github"></i> View Code</a>
                    </div>
                </div>

                <div class="project-card fade-in fade-in-delay-2">
                    <div class="project-icon"><i class="fas fa-database"></i></div>
                    <h3>Pandas Data Analysis Toolkit</h3>
                    <p>Comprehensive data analysis library built with Pandas covering data cleaning, transformation, merging, grouping, and exploratory analysis. Includes practical examples and reusable functions.</p>
                    <div class="project-tech">
                        <span>Python</span><span>Pandas</span><span>NumPy</span><span>Matplotlib</span>
                    </div>
                    <div class="project-links">
                        <a href="https://github.com/tayyaba-code/Pandas-basics" target="_blank" rel="noopener"><i class="fab fa-github"></i> View Code</a>
                    </div>
                </div>
            </div>
        </div>
    </section>

    <!-- ====== PUBLICATIONS ====== -->
    <section id="publications">
        <div class="section-inner">
            <div class="section-header">
                <div class="section-number">05 — Research</div>
                <h2 class="section-heading">Published <span class="gradient-text">work</span></h2>
                <p class="section-sub">Research at the intersection of AI and healthcare — all currently under peer review.</p>
            </div>

            <div class="pub-card fade-in">
                <div class="pub-title">Intelligent Detection of Blood Pressure Abnormalities Using Advanced Machine Learning Frameworks</div>
                <div class="pub-venue">Springer</div>
                <span class="pub-status under-review">Under Review · 2026</span>
            </div>

            <div class="pub-card fade-in fade-in-delay-1">
                <div class="pub-title">A Comparative Study of Supervised Machine Learning Methods for Stroke Prediction</div>
                <div class="pub-venue">Peer-Reviewed Journal</div>
                <span class="pub-status under-review">Under Review · 2025–26</span>
            </div>

            <div class="pub-card fade-in fade-in-delay-2">
                <div class="pub-title">Comparative Analysis of Machine Learning Models for Early Prediction of Diabetes Mellitus in Women</div>
                <div class="pub-venue">Peer-Reviewed Journal</div>
                <span class="pub-status under-review">Under Review · 2025–26</span>
            </div>
        </div>
    </section>

    <!-- ====== LEADERSHIP & AWARDS ====== -->
    <section id="leadership" style="background:var(--bg-alt);">
        <div class="section-inner">
            <div class="section-header">
                <div class="section-number">06 — Leadership &amp; Recognition</div>
                <h2 class="section-heading">Beyond the <span class="gradient-text">code</span></h2>
                <p class="section-sub">Leading initiatives that make a tangible difference — from IEEE to blood donation drives.</p>
            </div>

            <div class="lead-grid" style="margin-bottom:40px;">
                <div class="lead-card fade-in">
                    <div class="lead-icon"><i class="fas fa-award"></i></div>
                    <h3>Managing Director</h3>
                    <div class="lead-org-date">IEEE Society · UET Lahore · Jan 2026 — Present</div>
                    <p>Directing research initiatives across student chapters, sourcing three industry speakers, and growing outreach event attendance by 40%. Coordinated networking sessions connecting 100+ students with AI/tech professionals.</p>
                </div>
                <div class="lead-card fade-in fade-in-delay-1">
                    <div class="lead-icon"><i class="fas fa-tools"></i></div>
                    <h3>Technical Director</h3>
                    <div class="lead-org-date">Institute of Engineering &amp; Technology · UET · Sep 2025 — May 2026</div>
                    <p>Managed end-to-end technical delivery for six student engineering events. Led a 12-person cross-functional team with zero missed deadlines. Mentored junior members in project scoping and development.</p>
                </div>
                <div class="lead-card fade-in fade-in-delay-2">
                    <div class="lead-icon"><i class="fas fa-hand-holding-heart"></i></div>
                    <h3>Girls Coordinator</h3>
                    <div class="lead-org-date">Blood Donor Society · UET Lahore · Sep 2025 — May 2026</div>
                    <p>Increased registered female volunteer count by 30% across two semesters through targeted outreach and structured onboarding. Organized blood donation drives and awareness campaigns.</p>
                </div>
            </div>

            <div class="section-heading" style="font-size:1.5rem; margin-bottom:24px;">
                <span class="gradient-text-4">Honours &amp; Awards</span>
            </div>
            <div class="awards-grid">
                <div class="award-card fade-in">
                    <div class="award-icon"><i class="fas fa-trophy"></i></div>
                    <div>
                        <h4>Hoonhar Scholarship &amp; Prime Minister's Laptop</h4>
                        <p>Full merit-based award — top academic performers nationwide, 2026</p>
                    </div>
                </div>
                <div class="award-card fade-in fade-in-delay-1">
                    <div class="award-icon"><i class="fas fa-star"></i></div>
                    <div>
                        <h4>Academic Excellence — Dean's List</h4>
                        <p>CGPA 3.76/4.00 in BS Biomedical Engineering · UET Lahore</p>
                    </div>
                </div>
                <div class="award-card fade-in fade-in-delay-2">
                    <div class="award-icon"><i class="fas fa-certificate"></i></div>
                    <div>
                        <h4>AI for Medical Diagnosis — DeepLearning.AI</h4>
                        <p>Stanford University · IBM Generative AI Engineering · Coursera</p>
                    </div>
                </div>
            </div>
        </div>
    </section>

    <!-- ====== CONTACT ====== -->
    <section id="contact">
        <div class="section-inner">
            <div class="section-header">
                <div class="section-number">07 — Contact</div>
                <h2 class="section-heading">Let's <span class="gradient-text-2">build</span> something</h2>
                <p class="section-sub">Whether you have a project in mind, a research collaboration, or just want to connect — I'd love to hear from you.</p>
            </div>
            <div class="contact-grid">
                <div class="contact-info">
                    <p>
                        I'm always open to interesting conversations, collaborations, and opportunities 
                        where I can apply biomedical + AI engineering to solve real problems. 
                        Currently seeking ML/AI engineering roles and research collaborations.
                    </p>
                    <div class="contact-detail">
                        <i class="fas fa-envelope"></i>
                        <a href="mailto:sajjadtayyaba91@gmail.com">sajjadtayyaba91@gmail.com</a>
                    </div>
                    <div class="contact-detail">
                        <i class="fas fa-phone"></i>
                        <span>+92-303-9472753</span>
                    </div>
                    <div class="contact-detail">
                        <i class="fab fa-github"></i>
                        <a href="https://github.com/tayyaba-code" target="_blank">github.com/tayyaba-code</a>
                    </div>
                    <div class="contact-detail">
                        <i class="fab fa-linkedin-in"></i>
                        <a href="https://linkedin.com/in/tayyabasajjad" target="_blank">linkedin.com/in/tayyabasajjad</a>
                    </div>
                    <div class="contact-detail">
                        <i class="fas fa-map-marker-alt"></i>
                        <span>Lahore, Pakistan</span>
                    </div>
                </div>
                <div>
                    <!-- Formspree setup: 1) Sign up free at formspree.io 2) Create a form 3) Replace YOUR_FORM_ID below -->
                    <form class="contact-form" id="contactForm" action="https://formspree.io/f/YOUR_FORM_ID" method="POST">
                        <input type="text" name="name" placeholder="Your Name" autocomplete="name" required />
                        <input type="email" name="email" placeholder="Your Email" autocomplete="email" required />
                        <input type="text" name="subject" placeholder="Subject" autocomplete="off" />
                        <textarea name="message" placeholder="Your Message" autocomplete="off" required></textarea>
                        <button type="submit" class="btn btn-primary">Send Message <i class="fas fa-paper-plane"></i></button>
                    </form>
                    <div class="form-success" id="formSuccess">
                        <i class="fas fa-check-circle"></i> Thanks for reaching out! I'll get back to you within 24 hours.
                    </div>
                </div>
            </div>
        </div>
    </section>

    <!-- ====== FOOTER ====== -->
    <footer>
        <p>&copy; 2026 Tayyaba Sajjad. Biomedical Engineer &amp; AI/ML Engineer.</p>
        <div class="social-links">
            <a href="https://github.com/tayyaba-code" target="_blank" aria-label="GitHub"><i class="fab fa-github"></i></a>
            <a href="https://linkedin.com/in/tayyabasajjad" target="_blank" aria-label="LinkedIn"><i class="fab fa-linkedin-in"></i></a>
            <a href="mailto:sajjadtayyaba91@gmail.com" aria-label="Email"><i class="fas fa-envelope"></i></a>
        </div>
    </footer>

    <script>
        // Navbar scroll effect
        const navbar = document.getElementById('navbar');
        window.addEventListener('scroll', () => {{
            navbar.classList.toggle('scrolled', window.scrollY > 60);
        }});

        // Fade-in on scroll
        const observer = new IntersectionObserver((entries) => {{
            entries.forEach(entry => {{
                if (entry.isIntersecting) {{
                    entry.target.classList.add('visible');
                }}
            }});
        }}, {{ threshold: 0.1 }});

        document.querySelectorAll('.fade-in').forEach(el => observer.observe(el));

        // Contact form — opens email client immediately (no setup needed)
        const contactForm = document.getElementById('contactForm');
        const formSuccess = document.getElementById('formSuccess');

        contactForm.addEventListener('submit', function(e) {{
            e.preventDefault();

            const name = this.querySelector('input[name="name"]').value;
            const email = this.querySelector('input[name="email"]').value;
            const subject = this.querySelector('input[name="subject"]').value || 'Portfolio Inquiry';
            const message = this.querySelector('textarea[name="message"]').value;

            const submitBtn = this.querySelector('button[type="submit"]');
            const originalText = submitBtn.innerHTML;
            submitBtn.innerHTML = '<i class="fas fa-spinner fa-spin"></i> Opening email...';
            submitBtn.disabled = true;

            // Always use mailto so messages arrive immediately
            const fullBody = 'From: ' + name + ' (' + email + ')\n\n' + message;
            const mailtoLink = 'mailto:sajjadtayyaba91@gmail.com?subject='
                + encodeURIComponent(subject + ' - from ' + name)
                + '&body=' + encodeURIComponent(fullBody);
            window.open(mailtoLink, '_blank');

            this.style.display = 'none';
            formSuccess.classList.add('show');
            formSuccess.innerHTML = '<i class="fas fa-check-circle"></i> Your email client has been opened. Just hit send!';

            submitBtn.innerHTML = originalText;
            submitBtn.disabled = false;
        }});
    </script>
</body>
</html>'''

# Write the file
with open(r'C:\Users\sajja\Desktop\kai_data\portfolio.html', 'w', encoding='utf-8') as f:
    f.write(html)

print(f'SUCCESS: Written {len(html)} bytes')
print('Ends with </html>:', html.strip().endswith('</html>'))
