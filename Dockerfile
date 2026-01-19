# ⚠️ EXTREME DANGER: For prank/stress testing only. Use at your own risk.
# 면책사항: 장난 및 테스트용 패키지입니다. 사용 시 주의하십시오.

FROM python:3.12-slim

# Install system dependencies for audio (though Docker containers usually don't have speakers)
RUN apt-get update && apt-get install -y \
    aplay \
    alsa-utils \
    && rm -rf /var/lib/apt/lists/*

WORKDIR /app

# Copy the package files
COPY . .

# Install the package
RUN pip install . --break-system-packages

# Copy the test script
COPY test_emergency.py .

# Run the test by default (this will trigger the madness inside the container)
CMD ["python", "test_emergency.py"]
