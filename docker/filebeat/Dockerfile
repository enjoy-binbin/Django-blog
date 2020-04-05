FROM docker.elastic.co/beats/filebeat:7.6.0

# Copy our custom configuration file
COPY docker/filebeat/filebeat.yml /usr/share/filebeat/filebeat.yml

USER root
RUN chown root:filebeat /usr/share/filebeat/filebeat.yml
USER filebeat