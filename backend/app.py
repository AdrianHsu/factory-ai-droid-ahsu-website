from flask import Flask, jsonify
from flask_cors import CORS

app = Flask(__name__)
CORS(app)

resume_data = {
    "name": "Pin-Chun (Adrian) Hsu",
    "phone": "(+1) 213-618-2606",
    "email": "adrianhsu1995@gmail.com",
    "linkedin": "Adrian Hsu",
    "location": "San Francisco",
    "experience": [
        {
            "company": "xAI",
            "location": "San Francisco, CA",
            "positions": [
                {
                    "title": "Member of Technical Staff & Tech Lead Manager",
                    "period": "Jun. 2025 - Dec. 2025",
                    "bullets": [
                        "Algorithm Team (Organic & Ads) — Shopping Ads Lead. Managed a team of 4 to build Shopping Ads personalized algorithm from 0 to 1; drove multi-million dollar daily revenue growth during Prime Day and Black Friday.",
                        "Bootstrapped multiple Grok classification and ranking pipelines: Commerce Intent Detector that extracts purchase signals from organic engagements to drive Ads performance; Ads Reviewer that intercepts inappropriate creatives; Reply Re-ranker that sections low-quality content including crypto-spam, self-promotion, NSFW, and AI-generated content.",
                        "Shipped a Semantic ID retrieval system for Shopping Ads using RQ-VAE to encode 30-day user history, overcoming cold-start constraints via content-based signals to drive enhanced personalization.",
                        "Built a Generative AI augmented retrieval source to surface contextually relevant products with synthetic search queries and VectorDB.",
                        "Partnered with Human Agent team to scale up & improve recall of the evaluation system for LLM pipelines."
                    ]
                },
                {
                    "title": "Staff Software Engineer & Tech Lead Manager",
                    "period": "Sep. 2024 - Jul. 2025",
                    "bullets": [
                        "Applied AI Team — Search & Reply Lead. Managed a team of 3, driving >50% increase in engagement (Fav, Reply), >3% search DAU and UAM YoY.",
                        "Built Two-Tower Search Embedding Retrieval (Training, Indexing, Serving) based on xAI semantic embeddings and vector DB.",
                        "Shipped the on-prem ML ranker for Tweet Search and User Search from 0 to 1. Built Kafka pipelines for client event collection, feature logging, and MapReduce-based training data generation.",
                        "Modernized Reply serving stack by deprecating legacy infra and migrating to the xAI ecosystem, reducing technical debt."
                    ]
                },
                {
                    "title": "Software Engineer",
                    "period": "Jan. 2021 - Sep. 2024",
                    "bullets": [
                        "Timeline Team. Despite >85% workforce reduction following Twitter acquisition, I served as a primary owner of the Recommendation Org, maintaining critical infra stability for DAU and UAM.",
                        "Took sole ownership of Earlybird (Lucene) search index, ElasticSearch indexes following the elimination of the Search team.",
                        "Sprinted on multiple Elon direct requests: Pinned Tweet Broadcast feature on Home Timeline (via FanoutService); L1 ranker for Home Timeline by knowledge distillation to achieve end-to-end ML; Limit NSFW search results for non-NSFW queries.",
                        "Migrated to a new In-Network candidate source for Home Timeline built on Lucene Index that saved over 100K CPU cores per DC.",
                        "Shipped CrMixer, the centralized Out-of-Network serving infra handling millions of tweets/sec across Home Timeline, Explore, and Notifications."
                    ]
                }
            ]
        },
        {
            "company": "Twitter",
            "location": "Los Angeles, CA",
            "positions": [
                {
                    "title": "Software Engineer Intern",
                    "period": "Jun. 2020 - Sep. 2020",
                    "bullets": [
                        "Revenue Science Org, Ads Data Engineering Team",
                        "Built GCP data warehouse solutions and data pipelines to make Ads data better accessible and reliable."
                    ]
                }
            ]
        },
        {
            "company": "Alibaba Cloud",
            "location": "Hangzhou, China",
            "positions": [
                {
                    "title": "Software Engineer Intern",
                    "period": "Jul. 2018 - Oct. 2018",
                    "bullets": [
                        "Data Warehouse Team",
                        "Worked on the data warehouse backend, Dataworks, which supports the alibaba group including Taobao, Alipay, and more."
                    ]
                }
            ]
        }
    ],
    "education": [
        {
            "school": "University of California, Los Angeles (UCLA)",
            "location": "Los Angeles, CA",
            "degree": "M.S. in Computer Science",
            "period": "Sep. 2019 - Dec. 2020",
            "details": [
                "Overall GPA: 3.91/4.0. Specialized in Networking System & Distributed Computing",
                "Selected Coursework: Database Systems, Computer System Architecture, Big Data Systems, Distributed Systems (MIT 6.824, auditing)"
            ]
        },
        {
            "school": "National Taiwan University (NTU)",
            "location": "Taipei, Taiwan",
            "degree": "B.S. in Electrical Engineering",
            "period": "Sep. 2014 - Jan. 2019",
            "details": [
                "Overall GPA: 3.77/4.3, CS-Related GPA: 4.08/4.3 (3.92/4.0)",
                "President of NTUEE Student Association"
            ]
        }
    ],
    "skills": {
        "AI/ML": "Large-Scale Distributed Systems, Applied AI (SFT, Eval Framework), Recommendation Algorithms, Personalization, Ads Serving",
        "Retrieval": "Two-Tower Model (Training, Indexing, Serving), Semantic Id Retrieval, Embedding Search, Elasticsearch, Apache Lucene, RAG",
        "Data Pipeline": "Kafka, Spark, Polars, MapReduce, Hadoop, Flink",
        "Programming": "Python, Scala, Java, PyTorch, Rust, React, SQL, Protobuf, Thrift, gRPC",
        "Others": "Docker, Kubernetes, Qdrant, Nginx, Cargo, GCP, ONNX, GraphQL, uv"
    }
}

@app.route('/api/resume', methods=['GET'])
def get_resume():
    return jsonify(resume_data)

@app.route('/api/health', methods=['GET'])
def health():
    return jsonify({"status": "ok"})

if __name__ == '__main__':
    app.run(debug=True, port=5001)
