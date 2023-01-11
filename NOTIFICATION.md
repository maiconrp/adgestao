# Notificações

* Ultima Issue:
* Ultima Pull Request:
* Ultimo Commit

<!--

    - name: Pegar PRs
      run: |
        echo $(curl --request GET \
        --url https://api.github.com/repos/maiconrp/AD-gestao/issues?state=open \
        --header "content-type: application/json" \
        --header "authorization: Bearer ${{ secrets.GITHUB_TOKEN }}") | jq '.[] | .title, .user') > issue
    
    - name: Monta template
      run:
        printf "# Notificações\n * Ultima Issue\n * Ultima Pull Request\n * Ultimo Commit\n" > notification_template
        template = """
-->
"[BUG]: Teste de automatic notification issue" 60708311
"[BUG]: Teste de automatic notification issue" 60708311
