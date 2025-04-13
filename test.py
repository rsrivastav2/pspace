import win32com.client as win32

outlook = win32.Dispatch('outlook.application')
mail = outlook.CreateItem(0)
mail.To = 'someone@example.com'
mail.Subject = 'Selenium Report'
mail.HTMLBody = '<h2>Report</h2><p style="color:green;">All good!</p>'
mail.Send()
