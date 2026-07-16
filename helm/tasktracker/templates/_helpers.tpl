{{- define "tasktracker.backend.name" -}}
tasktracker-backend
{{- end -}}

{{- define "tasktracker.postgres.pvcName" -}}
{{ .Release.Name }}-{{ .Values.postgres.storage.claimName }}
{{- end -}}
