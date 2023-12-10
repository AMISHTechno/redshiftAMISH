```mermaid
graph TD
    A[Core Infrastructure]
    B[SysArch/Infra Service @ DCY(DataCentresYESSS) (Hédonism)]
    C[Dev/MLOps/DataEng @ JWTLive (Nullzero)]
    D[Bilateral Auth DCY<>JWTLiveModel]
    E[Log Data Generation @ DCY]
    F[Data Stored in ElasticDB]
    G[Model Training on AWS Lambda]
    H[CI/CD Control by DAG]
    I[Log Data Loglized]
    J[Data Engineering Pipeline Service]
    K[FastAPI Query to JWTLive ML Model]
    L[Analyzed Data Returned to DCY]
    M[Regular Model Training]
    N[Results in Elastic Search DB]
    O[Kibana Dashboard Display]
    P[Logs Stored in ElasticDB]
    Q[CI/CD Triggered by Code Changes]

    A --> B & C
    B --> D
    C -->|Receives Data| E
    E --> F
    F -->|Used in| G
    G -->|Deployed on| DCY
    DCY --> H
    H -->|Triggers| I & J & K
    I --> J
    J --> K
    K -->|Produces| L
    L -->|Triggers| M
    M -->|Updates| N
    N --> O
    DCY --> P
    P -->|Enhances| DCY
    Q --> H

    classDef default fill:#f9f,stroke:#333,stroke-width:2px;
    class A,B,C,D,E,F,G,H,I,J,K,L,M,N,O,P,Q default;
