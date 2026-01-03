const { useState, useEffect } = React;

const API_URL = 'http://localhost:5001/api';

function App() {
    const [resume, setResume] = useState(null);
    const [loading, setLoading] = useState(true);
    const [activeSection, setActiveSection] = useState('experience');
    const [error, setError] = useState(null);

    useEffect(() => {
        fetch(`${API_URL}/resume`)
            .then(res => res.json())
            .then(data => {
                setResume(data);
                setLoading(false);
            })
            .catch(err => {
                setError('Failed to load resume data. Make sure the backend is running.');
                setLoading(false);
            });
    }, []);

    if (loading) {
        return (
            <div className="loading">
                <div className="spinner"></div>
                Loading...
            </div>
        );
    }

    if (error) {
        return (
            <div className="loading">
                {error}
            </div>
        );
    }

    return (
        <div>
            <Header data={resume} />
            <Navigation active={activeSection} setActive={setActiveSection} />
            <div className="container">
                {activeSection === 'experience' && <Experience data={resume.experience} />}
                {activeSection === 'education' && <Education data={resume.education} />}
                {activeSection === 'skills' && <Skills data={resume.skills} />}
            </div>
            <Footer />
        </div>
    );
}

function Header({ data }) {
    return (
        <header className="header">
            <h1>{data.name}</h1>
            <p className="subtitle">Staff Software Engineer & Tech Lead Manager</p>
            <div className="contact-info">
                <span className="contact-item">
                    📍 {data.location}
                </span>
                <span className="contact-item">
                    📧 <a href={`mailto:${data.email}`}>{data.email}</a>
                </span>
                <span className="contact-item">
                    📞 {data.phone}
                </span>
                <span className="contact-item">
                    💼 <a href={`https://www.linkedin.com/in/${data.linkedin.toLowerCase().replace(' ', '')}`} target="_blank" rel="noopener noreferrer">LinkedIn</a>
                </span>
            </div>
        </header>
    );
}

function Navigation({ active, setActive }) {
    return (
        <nav className="nav">
            <button 
                className={`nav-btn ${active === 'experience' ? 'active' : ''}`}
                onClick={() => setActive('experience')}
            >
                Experience
            </button>
            <button 
                className={`nav-btn ${active === 'education' ? 'active' : ''}`}
                onClick={() => setActive('education')}
            >
                Education
            </button>
            <button 
                className={`nav-btn ${active === 'skills' ? 'active' : ''}`}
                onClick={() => setActive('skills')}
            >
                Skills
            </button>
        </nav>
    );
}

function Experience({ data }) {
    return (
        <section className="section">
            <h2 className="section-title">Work Experience</h2>
            {data.map((company, idx) => (
                <div key={idx} className="experience-card">
                    <div className="company-header">
                        <span className="company-name">{company.company}</span>
                        <span className="company-location">{company.location}</span>
                    </div>
                    {company.positions.map((position, pidx) => (
                        <div key={pidx} className="position">
                            <div className="position-title">{position.title}</div>
                            <div className="position-period">{position.period}</div>
                            <ul className="position-bullets">
                                {position.bullets.map((bullet, bidx) => (
                                    <li key={bidx}>{bullet}</li>
                                ))}
                            </ul>
                        </div>
                    ))}
                </div>
            ))}
        </section>
    );
}

function Education({ data }) {
    return (
        <section className="section">
            <h2 className="section-title">Education</h2>
            {data.map((edu, idx) => (
                <div key={idx} className="education-card">
                    <div className="school-header">
                        <span className="school-name">{edu.school}</span>
                        <span className="school-location">{edu.location}</span>
                    </div>
                    <div className="degree">{edu.degree}</div>
                    <div className="education-period">{edu.period}</div>
                    <ul className="education-details">
                        {edu.details.map((detail, didx) => (
                            <li key={didx}>{detail}</li>
                        ))}
                    </ul>
                </div>
            ))}
        </section>
    );
}

function Skills({ data }) {
    const skillIcons = {
        'AI/ML': '🤖',
        'Retrieval': '🔍',
        'Data Pipeline': '📊',
        'Programming': '💻',
        'Others': '🛠️'
    };

    return (
        <section className="section">
            <h2 className="section-title">Skills</h2>
            <div className="skills-grid">
                {Object.entries(data).map(([category, skills], idx) => (
                    <div key={idx} className="skill-category">
                        <div className="skill-title">
                            <span>{skillIcons[category] || '📌'}</span>
                            {category}
                        </div>
                        <div className="skill-tags">
                            {skills.split(', ').map((skill, sidx) => (
                                <span key={sidx} className="skill-tag">{skill}</span>
                            ))}
                        </div>
                    </div>
                ))}
            </div>
        </section>
    );
}

function Footer() {
    return (
        <footer className="footer">
            <p>© {new Date().getFullYear()} Pin-Chun (Adrian) Hsu. Built with React & Flask.</p>
        </footer>
    );
}

const root = ReactDOM.createRoot(document.getElementById('root'));
root.render(<App />);
