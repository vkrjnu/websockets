from django.shortcuts import render
from django.views.generic import View
from django.template import RequestContext
from fibo.models import Fibonacci
from django.http import Http404, JsonResponse
import time

# claas based view
class Fibo(View):
    def get(self, request):
        """
        Fibonacci series
        :param request:
        :return:
        """
        context = RequestContext(request, {})
        return render(request, 'fibo/fibo.html', context_instance=context)

    def post(self, request):
        """
        Ajax post
        :param request:
        :return:
        """
        if request.is_ajax():
            start = time.time()
            if request.POST.get('number', False):
                num = request.POST.get('number', 0)
                num = int(num)
                if Fibonacci.objects.filter(num=num).exists():
                    fibo = Fibonacci.objects.get(num=num)
                    output = fibo.output
                else:
                    output = self.calculate_fibo(num)
                    Fibonacci.objects.create(num=num, output=output)
                time_taken = time.time() - start
                return JsonResponse({'output':output, 'time_taken' : time_taken})
            else:
                raise Http404('Not a valid nnumber')
        else:
            raise Http404('Not a valid request.')

    def calculate_fibo(self, n):
        """
        Calculate fibonacci
        :param n:
        :return:
        """
        a, b = 1, 1
        for _ in range(n):
            a, b = b, a + b
        return a